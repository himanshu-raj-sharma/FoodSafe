package com.foodsafe.app.core.sync

import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow

enum class SyncState {
    PENDING, SYNCING, SYNCED, FAILED, CONFLICT
}

data class SyncOperation(
    val id: String,
    val type: SyncOperationType,
    val entityType: String,
    val entityId: String?,
    val data: Map<String, Any>,
    val timestamp: Long = System.currentTimeMillis(),
    var state: SyncState = SyncState.PENDING,
    var retryCount: Int = 0,
    val maxRetries: Int = 5,
)

enum class SyncOperationType {
    CREATE, UPDATE, DELETE, UPLOAD, DOWNLOAD
}

class SyncEngine {
    private val pendingOperations = mutableListOf<SyncOperation>()
    private val _syncState = MutableStateFlow<SyncState>(SyncState.SYNCED)
    val syncState: Flow<SyncState> = _syncState

    fun addOperation(operation: SyncOperation) {
        pendingOperations.add(operation)
        _syncState.value = SyncState.PENDING
    }

    fun addOperations(operations: List<SyncOperation>) {
        pendingOperations.addAll(operations)
        _syncState.value = SyncState.PENDING
    }

    fun getPendingOperations(): List<SyncOperation> {
        return pendingOperations.filter { it.state == SyncState.PENDING }
    }

    fun getFailedOperations(): List<SyncOperation> {
        return pendingOperations.filter { it.state == SyncState.FAILED }
    }

    fun markAsSyncing(operationId: String) {
        pendingOperations.find { it.id == operationId }?.let {
            it.state = SyncState.SYNCING
            _syncState.value = SyncState.SYNCING
        }
    }

    fun markAsSynced(operationId: String) {
        pendingOperations.find { it.id == operationId }?.let {
            it.state = SyncState.SYNCED
            if (pendingOperations.none { it.state == SyncState.PENDING || it.state == SyncState.SYNCING || it.state == SyncState.FAILED }) {
                _syncState.value = SyncState.SYNCED
            }
        }
    }

    fun markAsFailed(operationId: String) {
        pendingOperations.find { it.id == operationId }?.let {
            it.state = SyncState.FAILED
            _syncState.value = SyncState.FAILED
        }
    }

    fun getConflicts(): List<SyncOperation> {
        return pendingOperations.filter { it.state == SyncState.CONFLICT }
    }

    suspend fun retryFailedOperations(retryCallback: suspend (SyncOperation) -> Boolean) {
        val failed = getFailedOperations()
        for (operation in failed) {
            if (operation.retryCount < operation.maxRetries) {
                operation.retryCount++
                markAsSyncing(operation.id)
                val success = retryCallback(operation)
                if (success) {
                    markAsSynced(operation.id)
                } else {
                    markAsFailed(operation.id)
                }
            }
        }
    }

    fun reset() {
        pendingOperations.clear()
        _syncState.value = SyncState.SYNCED
    }
}
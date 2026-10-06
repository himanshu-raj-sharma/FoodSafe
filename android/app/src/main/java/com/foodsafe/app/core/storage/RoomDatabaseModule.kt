package com.foodsafe.app.core.storage

import com.foodsafe.app.core.database.FoodSafeDatabase
import com.foodsafe.app.core.database.entities.*
import com.foodsafe.app.core.sync.SyncOperation
import com.foodsafe.app.core.sync.SyncOperationType
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow

abstract class RoomStorage {
    abstract val db: FoodSafeDatabase

    abstract val organizationEntityFlow: Flow<List<OrganizationEntity>>
    abstract val outletEntityFlow: Flow<List<OutletEntity>>
    abstract val userEntityFlow: Flow<List<UserEntity>>
    abstract val incidentEntityFlow: Flow<List<IncidentEntity>>

    abstract suspend fun saveOrganization(organization: OrganizationEntity)
    abstract suspend fun saveOutlet(outlet: OutletEntity)
    abstract suspend fun saveUser(user: UserEntity)
    abstract suspend fun saveIncident(incident: IncidentEntity)

    abstract suspend fun deleteOrganization(organization: OrganizationEntity)
    abstract suspend fun deleteOutlet(outlet: OutletEntity)
    abstract suspend fun deleteUser(user: UserEntity)
    abstract suspend fun deleteIncident(incident: IncidentEntity)

    abstract suspend fun saveSyncOperation(operation: SyncOperation)
    abstract suspend fun updateSyncOperationState(operationId: String, state: SyncState)
    abstract suspend fun deleteSyncOperation(operationId: String)

    abstract val pendingOperations: Flow<List<SyncOperation>>
    abstract val syncState: Flow<SyncState>

    abstract suspend fun resetSync()
}
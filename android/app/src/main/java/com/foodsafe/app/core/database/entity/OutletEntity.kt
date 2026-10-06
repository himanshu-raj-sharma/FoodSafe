package com.foodsafe.app.core.database.entities

import androidx.room.Entity
import androidx.room.PrimaryKey
import androidx.room.Index

@Entity(
    tableName = "outlets",
    indices = [
        Index("organization_id"),
        Index("code"),
    ]
)
data class OutletEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val organizationId: Long,
    val name: String,
    val code: String,
    val address: String?,
    val contactPerson: String?,
    val contactPhone: String?,
    val latitude: String?,
    val longitude: String?,
    val isActive: Boolean = true,
    val createdAt: Long = System.currentTimeMillis(),
    val updatedAt: Long = System.currentTimeMillis(),
    val deletedAt: Long? = null,
)
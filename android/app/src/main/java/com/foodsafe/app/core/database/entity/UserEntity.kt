package com.foodsafe.app.core.database.entities

import androidx.room.Entity
import androidx.room.PrimaryKey
import androidx.room.Index

@Entity(
    tableName = "users",
    indices = [
        Index("email"),
        Index("organization_id"),
    ]
)
data class UserEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val organizationId: Long,
    val username: String,
    val email: String,
    val passwordHash: String,
    val firstName: String?,
    val lastName: String?,
    val phone: String?,
    val isActive: Boolean = true,
    val isVerified: Boolean = false,
    val lastLoginAt: Long?,
    val createdAt: Long = System.currentTimeMillis(),
    val updatedAt: Long = System.currentTimeMillis(),
    val deletedAt: Long? = null,
)
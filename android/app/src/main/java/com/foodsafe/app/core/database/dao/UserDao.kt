package com.foodsafe.app.core.database.dao

import androidx.room.*
import com.foodsafe.app.core.database.entities.UserEntity
import kotlinx.coroutines.flow.Flow

@Dao
interface UserDao {
    @Query("SELECT * FROM users WHERE id = :id")
    fun getById(id: Long): UserEntity?

    @Query("SELECT * FROM users WHERE email = :email AND organization_id = :organizationId")
    fun getByEmail(email: String, organizationId: Long): UserEntity?

    @Query("SELECT * FROM users WHERE organization_id = :organizationId AND deleted_at IS NULL")
    fun getByOrganization(organizationId: Long): Flow<List<UserEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(user: UserEntity): Long

    @Update
    suspend fun update(user: UserEntity)

    @Delete
    suspend fun delete(user: UserEntity)
}
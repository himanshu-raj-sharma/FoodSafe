package com.foodsafe.app.core.database.dao

import androidx.room.*
import com.foodsafe.app.core.database.entities.OrganizationEntity
import kotlinx.coroutines.flow.Flow

@Dao
interface OrganizationDao {
    @Query("SELECT * FROM organizations WHERE id = :id")
    fun getById(id: Long): OrganizationEntity?

    @Query("SELECT * FROM organizations WHERE slug = :slug")
    fun getBySlug(slug: String): OrganizationEntity?

    @Query("SELECT * FROM organizations WHERE deleted_at IS NULL")
    fun getAll(): Flow<List<OrganizationEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(organization: OrganizationEntity): Long

    @Update
    suspend fun update(organization: OrganizationEntity)

    @Delete
    suspend fun delete(organization: OrganizationEntity)
}
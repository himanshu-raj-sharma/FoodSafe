package com.foodsafe.app.core.database.dao

import androidx.room.*
import com.foodsafe.app.core.database.entities.OutletEntity
import kotlinx.coroutines.flow.Flow

@Dao
interface OutletDao {
    @Query("SELECT * FROM outlets WHERE organization_id = :organizationId AND deleted_at IS NULL")
    fun getByOrganization(organizationId: Long): Flow<List<OutletEntity>>

    @Query("SELECT * FROM outlets WHERE id = :id AND deleted_at IS NULL")
    fun getById(id: Long): OutletEntity?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(outlet: OutletEntity): Long

    @Update
    suspend fun update(outlet: OutletEntity)

    @Delete
    suspend fun delete(outlet: OutletEntity)
}
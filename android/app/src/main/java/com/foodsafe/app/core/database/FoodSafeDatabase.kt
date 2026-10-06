package com.foodsafe.app.core.database

import androidx.room.Database
import androidx.room.RoomDatabase
import com.foodsafe.app.core.database.dao.*
import com.foodsafe.app.core.database.entities.*

@Database(
    entities = [
        Organization::class,
        Outlet::class,
        User::class,
        Task::class,
        TaskCompletion::class,
        Incident::class,
        IncidentEvidence::class,
        CorrectiveAction::class,
        Supplier::class,
        Delivery::class,
        Batch::class,
        TraceabilityEvent::class,
        Recall::class,
        AuditPack::class,
        Notification::class,
        SyncRecord::class,
        AuditLog::class,
    ],
    version = 1,
    exportSchema = false
)
abstract class FoodSafeDatabase : RoomDatabase() {

    abstract fun organizationDao(): OrganizationDao
    abstract fun outletDao(): OutletDao
    abstract fun userDao(): UserDao
    abstract fun taskDao(): TaskDao
    abstract fun taskCompletionDao(): TaskCompletionDao
    abstract fun incidentDao(): IncidentDao
    abstract fun incidentEvidenceDao(): IncidentEvidenceDao
    abstract fun correctiveActionDao(): CorrectiveActionDao
    abstract fun supplierDao(): SupplierDao
    abstract fun deliveryDao(): DeliveryDao
    abstract fun batchDao(): BatchDao
    abstract fun traceabilityEventDao(): TraceabilityEventDao
    abstract fun recallDao(): RecallDao
    abstract fun auditPackDao(): AuditPackDao
    abstract fun notificationDao(): NotificationDao
    abstract fun syncRecordDao(): SyncRecordDao
    abstract fun auditLogDao(): AuditLogDao

    companion object {
        @Volatile
        private var INSTANCE: FoodSafeDatabase? = null

        fun getInstance(context: android.content.Context): FoodSafeDatabase {
            return INSTANCE ?: synchronized(this) {
                val instance = androidx.room.Room.databaseBuilder(
                    context.applicationContext,
                    FoodSafeDatabase::class.java,
                    "foodsafe_database"
                )
                    .fallbackToDestructiveMigration()
                    .build()
                INSTANCE = instance
                instance
            }
        }
    }
}
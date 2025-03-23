import sqlite3
import pandas as pd

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect("chinook.db")

# Har bir mijoz qancha pul sarflaganini aniqlash
query = """
    SELECT c.CustomerId, c.FirstName, c.LastName, SUM(i.Total) AS TotalSpent
    FROM Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
    GROUP BY c.CustomerId
    ORDER BY TotalSpent DESC
    LIMIT 5;
"""
top_customers = pd.read_sql(query, conn)

print("Eng ko‘p xarid qilgan 5 mijoz:")
print(top_customers)



# Mijozlar tomonidan sotib olingan trek va albomlarni aniqlash
query = """
    WITH CustomerTrack AS (
        SELECT il.InvoiceId, i.CustomerId, t.AlbumId, COUNT(il.TrackId) AS TracksBought
        FROM InvoiceLine il
        JOIN Invoice i ON il.InvoiceId = i.InvoiceId
        JOIN Track t ON il.TrackId = t.TrackId
        GROUP BY il.InvoiceId, i.CustomerId, t.AlbumId
    ),
    AlbumTrackCounts AS (
        SELECT AlbumId, COUNT(TrackId) AS AlbumTracks
        FROM Track
        GROUP BY AlbumId
    )
    SELECT 
        ct.CustomerId,
        CASE 
            WHEN ct.TracksBought = atc.AlbumTracks THEN 'Full Album'
            ELSE 'Individual Tracks'
        END AS PurchaseType
    FROM CustomerTrack ct
    JOIN AlbumTrackCounts atc ON ct.AlbumId = atc.AlbumId;
"""

purchase_data = pd.read_sql(query, conn)

# Har bir turdagi mijoz foizini hisoblash
purchase_summary = purchase_data["PurchaseType"].value_counts(normalize=True) * 100

print("Albom va trek xaridlari bo‘yicha taqsimot (%):")
print(purchase_summary)

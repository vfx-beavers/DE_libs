BULK INSERT STAGE.Snapshot.S15_csv_RU_CALL FROM 'c:\install\data\RU_CALL_Feb2024-02.2024_combined.csv'
with
(
    firstrow =2,
    BATCHSIZE = 100000,
    fieldterminator = ';',
    rowterminator = '\n',
    CODEPAGE = '65001',
    DATAFILETYPE = 'Char',
    ERRORFILE = 'c:\install\data\RU_CALL_Feb2024-02.2024_combined_ERROR.log',
    tablock
);
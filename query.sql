CREATE TABLE customer  
(  
    CustomerID uniqueidentifier NOT NULL PRIMARY KEY DEFAULT newid(),  
    Company varchar(30) NOT NULL,  
    ContactName varchar(60) NOT NULL,   
    Address varchar(30) NOT NULL,   
    City varchar(30) NOT NULL,  
    Telephone varchar(15) NOT NULL,  
    Mail varchar(30) NOT NULL,
    Retail BIT DEFAULT 0,
    NIP INT NULL
);  
GO
CREATE TABLE headOrder (
    headOrderID uniqueidentifier NOT NULL PRIMARY KEY DEFAULT newid(),
    dataOrder DATE NOT NULL DEFAULT GETDATE(),
    CustomerID uniqueidentifier NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);
GO

CREATE TABLE Orders(
    OrdersID uniqueidentifier NOT NULL PRIMARY KEY DEFAULT newid(),
    headOrderID uniqueidentifier NOT NULL,
    productID INT NOT NULL,
    amount INT NOT NULL CHECK ( amount > 0 ),
    price MONEY NOT NULL CHECK (price > 0),
    FOREIGN KEY (headOrderID) REFERENCES headOrder(headOrderID),
    FOREIGN KEY (productID) REFERENCES product(productID)
);
GO
CREATE TABLE product(
productID INT NOT NULL PRIMARY KEY IDENTITY,
nameProduct VARCHAR(100) NOT NULL,
)
GO

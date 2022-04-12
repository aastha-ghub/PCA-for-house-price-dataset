#!/usr/bin/env python
# coding: utf-8

#   <tr>
#         <td>
#             <div align="left">
#                 <font size=25px>
#                     <b>Dimension Reduction Techniques (PCA)
#                     </b>
#                 </font>
#             </div>
#         </td>
#     </tr>

# ## Problem Statement:
# A key challenge for property sellers is to determine the sale price of the property. The ability to predict the exact property value is beneficial for property investors as well as for buyers to plan their finances according to the price trend. The property prices depend on the number of features like the property area, basement square footage, year built, number of bedrooms, and others. The prices can be predicted more accurately if the number of predictors is less. Several dimension reduction techniques are being applied to decrease this number of predictors.

# ## Data Definition:
# 
# Input variables:
# 
# **1.MSSubClass:** Identifies the type of dwelling involved in the sale
# 
#         20	1-STORY 1946 & NEWER ALL STYLES
#         30	1-STORY 1945 & OLDER
#         40	1-STORY W/FINISHED ATTIC ALL AGES
#         45	1-1/2 STORY - UNFINISHED ALL AGES
#         50	1-1/2 STORY FINISHED ALL AGES
#         60	2-STORY 1946 & NEWER
#         70	2-STORY 1945 & OLDER
#         75	2-1/2 STORY ALL AGES
#         80	SPLIT OR MULTI-LEVEL
#         85	SPLIT FOYER
#         90	DUPLEX - ALL STYLES AND AGES
#        120	1-STORY PUD (Planned Unit Development) - 1946 & NEWER
#        150	1-1/2 STORY PUD - ALL AGES
#        160	2-STORY PUD - 1946 & NEWER
#        180	PUD - MULTILEVEL - INCL SPLIT LEV/FOYER
#        190	2 FAMILY CONVERSION - ALL STYLES AND AGES
# 
# **2.MSZoning:** Identifies the general zoning classification of the sale
# 		
#        A	 Agriculture
#        C	 Commercial
#        FV	Floating Village Residential
#        I	 Industrial
#        RH	Residential High Density
#        RL	Residential Low Density
#        RP	Residential Low Density Park 
#        RM	Residential Medium Density
# 	
# **3.LotFrontage:** Linear feet of street connected to property
# 
# **4.LotArea:** Lot size is the lot or parcel side where it adjoins a street, boulevard or access way
# 
# **5.Street:** Type of road access to property
# 
#        Grvl	Gravel	
#        Pave	Paved
#        	
# **6.Alley:** Type of alley access to property
# 
#        Grvl	Gravel
#        Pave	Paved
#        NA 	 No alley access
# 		
# **7.LotShape:** General shape of property
# 
#        Reg	Regular	
#        IR1	Slightly irregular
#        IR2	Moderately Irregular
#        IR3	Irregular
#        
# **8.LandContour:** Flatness of the property
# 
#        Lvl	Near Flat/Level	
#        Bnk	Banked - Quick and significant rise from street grade to building
#        HLS	Hillside - Significant slope from side to side
#        Low	Depression
# 		
# **9.Utilities:** Type of utilities available
# 		
#        AllPub	All public Utilities (E,G,W,& S)	
#        NoSewr	Electricity, Gas, and Water (Septic Tank)
#        NoSeWa	Electricity and Gas Only
#        ELO	   Electricity only	
# 	
# **10.LotConfig:** Lot configuration
# 
#        Inside	Inside lot
#        Corner	Corner lot
#        CulDSac   Cul-de-sac
#        FR2	   Frontage on 2 sides of property
#        FR3	   Frontage on 3 sides of property
# 	
# **11.LandSlope:** Slope of property
# 		
#        Gtl	Gentle slope
#        Mod	Moderate Slope	
#        Sev	Severe Slope
# 	
# **12.Neighborhood:** Physical locations within Ames city limits
# 
#        Blmngtn	Bloomington Heights
#        Blueste	Bluestem
#        BrDale	 Briardale
#        BrkSide	Brookside
#        ClearCr	Clear Creek
#        CollgCr	College Creek
#        Crawfor	Crawford
#        Edwards	Edwards
#        Gilbert	Gilbert
#        IDOTRR	 Iowa DOT and Rail Road
#        MeadowV	Meadow Village
#        Mitchel	Mitchell
#        Names	  North Ames
#        NoRidge	Northridge
#        NPkVill	Northpark Villa
#        NridgHt	Northridge Heights
#        NWAmes	 Northwest Ames
#        OldTown	Old Town
#        SWISU	  South & West of Iowa State University
#        Sawyer	 Sawyer
#        SawyerW	Sawyer West
#        Somerst	Somerset
#        StoneBr	Stone Brook
#        Timber	 Timberland
#        Veenker	Veenker
# 			
# **13.Condition1:** Proximity to various conditions
# 	
#        Artery  Adjacent to arterial street
#        Feedr   Adjacent to feeder street	
#        Norm	Normal	
#        RRNn	Within 200' of North-South Railroad
#        RRAn	Adjacent to North-South Railroad
#        PosN	Near positive off-site feature--park, greenbelt, etc.
#        PosA	Adjacent to postive off-site feature
#        RRNe	Within 200' of East-West Railroad
#        RRAe	Adjacent to East-West Railroad
# 	
# **14.Condition2:** Proximity to various conditions (if more than one is present)
# 		
#        Artery      Adjacent to arterial street
#        Feedr       Adjacent to feeder street	
#        Norm	    Normal	
#        RRNn	    Within 200' of North-South Railroad
#        RRAn	    Adjacent to North-South Railroad
#        PosN	    Near positive off-site feature--park, greenbelt, etc.
#        PosA	    Adjacent to postive off-site feature
#        RRNe	    Within 200' of East-West Railroad
#        RRAe	    Adjacent to East-West Railroad
# 	
# **15.BldgType:** Type of dwelling
# 		
#        1Fam	  Single-family Detached	
#        2FmCon	Two-family Conversion; originally built as one-family dwelling
#        Duplx	 Duplex
#        TwnhsE	Townhouse End Unit
#        TwnhsI	Townhouse Inside Unit
# 	
# **16.HouseStyle:** Style of dwelling
# 	
#        1Story	One story
#        1.5Fin	One and one-half story: 2nd level finished
#        1.5Unf	One and one-half story: 2nd level unfinished
#        2Story	Two story
#        2.5Fin	Two and one-half story: 2nd level finished
#        2.5Unf	Two and one-half story: 2nd level unfinished
#        SFoyer	Split Foyer
#        SLvl	  Split Level
# 	
# **17.OverallQual:** Rates the overall material and finish of the house
# 
#        10   Very Excellent
#        9	Excellent
#        8	Very Good
#        7	Good
#        6	Above Average
#        5	Average
#        4	Below Average
#        3	Fair
#        2	Poor
#        1	Very Poor
# 	
# **18.OverallCond:** Rates the overall condition of the house
# 
#        10   Very Excellent
#        9	Excellent
#        8	Very Good
#        7	Good
#        6	Above Average	
#        5	Average
#        4	Below Average	
#        3	Fair
#        2	Poor
#        1	Very Poor
# 		
# **19.YearBuilt:** Original construction date
# 
# **20.YearRemodAdd:** Remodel date (same as construction date if no remodeling or additions)
# 
# **21.RoofStyle:** Type of roof
# 
#        Flat	   Flat
#        Gable	  Gable
#        Gambrel	Gabrel (Barn)
#        Hip	    Hip
#        Mansard	Mansard
#        Shed	   Shed
# 		
# **22.RoofMatl:** Roof material
# 
#        ClyTile	Clay or Tile
#        CompShg	Standard (Composite) Shingle
#        Membran	Membrane
#        Metal	  Metal
#        Roll	   Roll
#        Tar&Grv	Gravel & Tar
#        WdShake	Wood Shakes
#        WdShngl	Wood Shingles
# 		
# **23.Exterior1st:** Exterior covering on house
# 
#        AsbShng	Asbestos Shingles
#        AsphShn	Asphalt Shingles
#        BrkComm	Brick Common
#        BrkFace	Brick Face
#        CBlock	 Cinder Block
#        CemntBd	Cement Board
#        HdBoard	Hard Board
#        ImStucc	Imitation Stucco
#        MetalSd	Metal Siding
#        Other	  Other
#        Plywood	Plywood
#        PreCast	PreCast	
#        Stone	  Stone
#        Stucco	 Stucco
#        VinylSd	Vinyl Siding
#        Wd Sdng	Wood Siding
#        WdShing	Wood Shingles
# 	
# **24.Exterior2nd:** Exterior covering on house (if more than one material)
# 
#        AsbShng	Asbestos Shingles
#        AsphShn	Asphalt Shingles
#        BrkComm	Brick Common
#        BrkFace	Brick Face
#        CBlock	 Cinder Block
#        CemntBd	Cement Board
#        HdBoard	Hard Board
#        ImStucc	Imitation Stucco
#        MetalSd	Metal Siding
#        Other	  Other
#        Plywood	Plywood
#        PreCast	PreCast
#        Stone	  Stone
#        Stucco     Stucco
#        VinylSd	Vinyl Siding
#        Wd Sdng	Wood Siding
#        WdShing	Wood Shingles
# 	
# **25.MasVnrType:** Masonry veneer type
# 
#        BrkCmn     Brick Common
#        BrkFace	Brick Face
#        CBlock	 Cinder Block
#        None	   None
#        Stone      Stone
# 	
# **26.MasVnrArea:** Masonry veneer area in square feet
# 
# **27.ExterQual:** Evaluates the quality of the material on the exterior
# 		
#        Ex	Excellent
#        Gd	Good
#        TA	Average/Typical
#        Fa	Fair
#        Po	Poor
# 		
# **28.ExterCond:** Evaluates the present condition of the material on the exterior
# 		
#        Ex	Excellent
#        Gd	Good
#        TA	Average/Typical
#        Fa	Fair
#        Po	Poor
# 		
# **29.Foundation:** Type of foundation
# 		
#        BrkTil	Brick & Tile
#        CBlock	Cinder Block
#        PConc     Poured Contrete	
#        Slab	  Slab
#        Stone	 Stone
#        Wood	  Wood
# 		
# **30.BsmtQual:** Evaluates the height of the basement
# 
#        Ex	Excellent (100+ inches)	
#        Gd	Good (90-99 inches)
#        TA	Typical (80-89 inches)
#        Fa	Fair (70-79 inches)
#        Po	Poor (<70 inches
#        NA	No Basement
# 		
# **31.BsmtCond:** Evaluates the general condition of the basement
# 
#        Ex	Excellent
#        Gd	Good
#        TA	Typical - slight dampness allowed
#        Fa	Fair - dampness or some cracking or settling
#        Po	Poor - Severe cracking, settling, or wetness
#        NA	No Basement
# 	
# **32.BsmtExposure:** Refers to walkout or garden level walls
# 
#        Gd	Good Exposure
#        Av	Average Exposure (split levels or foyers typically score average or above)	
#        Mn	Mimimum Exposure
#        No	No Exposure
#        NA	No Basement
# 	
# **33.BsmtFinType1:** Rating of basement finished area
# 
#        GLQ	Good Living Quarters
#        ALQ	Average Living Quarters
#        BLQ	Below Average Living Quarters	
#        Rec	Average Rec Room
#        LwQ	Low Quality
#        Unf	Unfinshed
#        NA	 No Basement
# 		
# **34.BsmtFinSF1:** Type 1 finished square feet
# 
# **35.BsmtFinType2:** Rating of basement finished area (if multiple types)
# 
#        GLQ	Good Living Quarters
#        ALQ	Average Living Quarters
#        BLQ	Below Average Living Quarters	
#        Rec	Average Rec Room
#        LwQ	Low Quality
#        Unf	Unfinshed
#        NA	 No Basement
# 
# **36.BsmtFinSF2:** Type 2 finished square feet
# 
# **37.BsmtUnfSF:** Unfinished square feet of basement area
# 
# **38.TotalBsmtSF:** Total square feet of basement area
# 
# **39.Heating:** Type of heating
# 		
#        Floor   Floor Furnace
#        GasA	Gas forced warm air furnace
#        GasW	Gas hot water or steam heat
#        Grav	Gravity furnace	
#        OthW	Hot water or steam heat other than gas
#        Wall	Wall furnace
# 		
# **40.HeatingQC:** Heating quality and condition
# 
#        Ex	Excellent
#        Gd	Good
#        TA	Average/Typical
#        Fa	Fair
#        Po	Poor
# 		
# **41.CentralAir:** Central air conditioning
# 
#        N	No
#        Y	Yes
# 		
# **42.Electrical:** Electrical system
# 
#        SBrkr	Standard Circuit Breakers & Romex
#        FuseA	Fuse Box over 60 AMP and all Romex wiring (Average)	
#        FuseF	60 AMP Fuse Box and mostly Romex wiring (Fair)
#        FuseP	60 AMP Fuse Box and mostly knob & tube wiring (poor)
#        Mix	  Mixed
# 		
# **43.1stFlrSF:** First Floor square feet
#  
# **44.2ndFlrSF:** Second floor square feet
# 
# **45.LowQualFinSF:** Low quality finished square feet (all floors)
# 
# **46.GrLivArea:** Above grade (ground) living area square feet
# 
# **47.BsmtFullBath:** Basement full bathrooms
# 
# **48.BsmtHalfBath:** Basement half bathrooms
# 
# **49.FullBath:** Full bathrooms above grade
# 
# **50.HalfBath:** Half baths above grade
# 
# **51.BedroomAbvGr:** Bedrooms above grade (does NOT include basement bedrooms)
# 
# **52.KitchenAbvGr:** Kitchens above grade
# 
# **53.KitchenQual:** Kitchen quality
# 
#        Ex	Excellent
#        Gd	Good
#        TA	Typical/Average
#        Fa	Fair
#        Po	Poor
#        	
# **54.TotRmsAbvGrd:** Total rooms above grade (does not include bathrooms)
# 
# **55.Functional:** Home functionality (Assume typical unless deductions are warranted)
# 
#        Typ	Typical Functionality
#        Min1   Minor Deductions 1
#        Min2   Minor Deductions 2
#        Mod	Moderate Deductions
#        Maj1   Major Deductions 1
#        Maj2   Major Deductions 2
#        Sev	Severely Damaged
#        Sal	Salvage only
# 		
# **56.Fireplaces:** Number of fireplaces
# 
# **57.FireplaceQu:** Fireplace quality
# 
#        Ex	Excellent - Exceptional Masonry Fireplace
#        Gd	Good - Masonry Fireplace in main level
#        TA	Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement
#        Fa	Fair - Prefabricated Fireplace in basement
#        Po	Poor - Ben Franklin Stove
#        NA	No Fireplace
# 		
# **58.GarageType:** Garage location
# 		
#        2Types	More than one type of garage
#        Attchd	Attached to home
#        Basment   Basement Garage
#        BuiltIn   Built-In (Garage part of house - typically has room above garage)
#        CarPort   Car Port
#        Detchd	Detached from home
#        NA	    No Garage
# 		
# **59.GarageYrBlt:** Year garage was built
# 		
# **60.GarageFinish:** Interior finish of the garage
# 
#        Fin	Finished
#        RFn	Rough Finished	
#        Unf	Unfinished
#        NA	 No Garage
# 		
# **61.GarageCars:** Size of garage in car capacity
# 
# **62.GarageArea:** Size of garage in square feet
# 
# **63.GarageQual:** Garage quality
# 
#        Ex	Excellent
#        Gd	Good
#        TA	Typical/Average
#        Fa	Fair
#        Po	Poor
#        NA	No Garage
# 		
# **64.GarageCond:** Garage condition
# 
#        Ex	Excellent
#        Gd	Good
#        TA	Typical/Average
#        Fa	Fair
#        Po	Poor
#        NA	No Garage
# 		
# **65.PavedDrive:** Paved driveway
# 
#        Y	Paved 
#        P	Partial Pavement
#        N	Dirt/Gravel
# 		
# **66.WoodDeckSF:** Wood deck area in square feet
# 
# **67.OpenPorchSF:** Open porch area in square feet
# 
# **68.EnclosedPorch:** Enclosed porch area in square feet
# 
# **69.3SsnPorch:** Three season porch area in square feet
# 
# **70.ScreenPorch:** Screen porch area in square feet
# 
# **71.PoolArea:** Pool area in square feet
# 
# **72.PoolQC:** Pool quality
# 		
#        Ex	Excellent
#        Gd	Good
#        TA	Average/Typical
#        Fa	Fair
#        NA	No Pool
# 		
# **73.Fence:** Fence quality
# 		
#        GdPrv	Good Privacy
#        MnPrv	Minimum Privacy
#        GdWo	 Good Wood
#        MnWw	 Minimum Wood/Wire
#        NA	   No Fence
# 	
# **74.MiscFeature:** Miscellaneous feature not covered in other categories
# 		
#        Elev	Elevator
#        Gar2	2nd Garage (if not described in garage section)
#        Othr	Other
#        Shed	Shed (over 100 SF)
#        TenC	Tennis Court
#        NA	  None
# 		
# **75.MiscVal:** Value of miscellaneous feature
# 
# **76.MoSold:** Month Sold (MM)
# 
# **77.YrSold:** Year Sold (YYYY)
# 
# **78.SaleType: Type of sale**
# 		
#        WD 	Warranty Deed - Conventional
#        CWD	Warranty Deed - Cash
#        VWD	Warranty Deed - VA Loan
#        New	Home just constructed and sold
#        COD	Court Officer Deed/Estate
#        Con	Contract 15% Down payment regular terms
#        ConLw  Contract Low Down payment and low interest
#        ConLI  Contract Low Interest
#        ConLD  Contract Low Down
#        Oth	Other
# 		
# **79.SaleCondition:** Condition of sale
# 
#        Normal	Normal Sale
#        Abnorml   Abnormal Sale -  trade, foreclosure, short sale
#        AdjLand   Adjoining Land Purchase
#        Alloca    Allocation - two linked properties with separate deeds, typically condo with a garage unit	
#        Family	Sale between family members
#        Partial   Home was not completed when last assessed (associated with New Homes)

# ## Content
# 
# 1. **[Import Packages](#import_packages)**
# 2. **[Read Data](#Read_Data)**
# 3. **[Understand and Prepare the Data](#data_preparation)**
#     - 3.1 - [Data Types and Dimensions](#Data_Types)
#     - 3.2 - [Feature Engineering](#Feature_Engineering)
#     - 3.3 - [Missing Data Treatment](#Missing_Data_Treatment)
# 4. **[Compute Principal Component (from scratch)](#CPCS)**
#     - 4.1 - [Prepare the Data](#Data_Prepare)
#     - 4.2 - [Scale the Data](#Scale)
#     - 4.3 - [Covariance Matrix](#cov_mat)
#     - 4.4 - [Compute Eigenvalues and Eigenvectors](#eigen)
#     - 4.5 - [Decide Number of Principal Components](#components)
#     - 4.6 - [Calculate Principal Components](#pca)
# 5. **[Compute Principal Component (using sklearn)](#pcafunction)**
# 6. **[Conclusion](#Conclusion)**
# 

# <a id='import_packages'></a>
# ## 1. Import Packages

# In[1]:


# 'Pandas' is used for data manipulation and analysis
import pandas as pd 

# 'Numpy' is used for mathematical operations on large, multi-dimensional arrays and matrices
import numpy as np

# 'Matplotlib' is a data visualization library for 2D and 3D plots, built on numpy
import matplotlib.pyplot as plt

# 'datetime' is used to perform date and time operations
import datetime as dt

# 'StandardScalar' from sklearn.preprocessing library is used to scale the data
from sklearn.preprocessing import StandardScaler

# 'eig' from numpy.linalg to calculate eigenvalues and eigenvectors
from numpy.linalg import eig

# 'PCA' function to perform principal component analysis using the sklearn library
from sklearn.decomposition import PCA


# <a id='Read_Data'></a>
# ## 2. Read the Data

# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="key.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                     <b>Read the data using read_csv() function from pandas<br> 
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# In[2]:


# read the data
raw_data = pd.read_csv('houseprice.csv')
# print the first five rows of the data
raw_data.head()


# <a id='data_preparation'></a>
# ## 3. Understand and Prepare the Data

# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="key.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                     <b>The process of data preparation entails cleansing, structuring and integrating data to make it ready for analysis. <br><br>
#                         Here we will analyze and prepare data to perform regression techniques:<br>
#                         1. Check dimensions and data types of the dataframe <br>
#                         2. Study summary statistics<br> 
#                         3. Check for missing values<br>
#                         4. Study correlation<br>
#                                        </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# #### Change index column
# 
# The first column in the data contains a unique numbering for each observation. We can make this column as an index column

# In[3]:


# the parameter 'index_col' will change the index to the specified column
raw_data = pd.read_csv('houseprice.csv', index_col=0)

# head() to display top five rows
raw_data.head()


# <a id='Data_Types'></a>
# ## 3.1 Data Types and Dimensions

# In[4]:


# check the data types for variables
raw_data.info()


# <table align='left'>
#     <tr>
#         <td width='8%'>
#             <img src='note.png'>
#         </td>
#         <td>
#             <div align='left', style='font-size:120%'>
#                     <b>From the above output, we see that not all the variables are numeric. Many variables, including the target variable are categorical variables<br>
#                     </br></b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# In[5]:


# get the shape
print(raw_data.shape)


# **We see the dataframe has 80 columns and 1460 observations**

# <table align='left'>
#     <tr>
#         <td width='8%'>
#             <img src='note.png'>
#         </td>
#         <td>
#             <div align='left', style='font-size:120%'>
#                     <b>From the above output, we see that the data type of the variables like 'MSSubclass', 'OverallQual', 'OverallCond' has 'int64' data type<br><br>
#                         But by data definition these are 'categorical' variables. So we will convert the data type of these variables  to object
#                     </br></b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# In[6]:


# Use .astype() to change the data type
# use 'for' loop to change the data type of a large number of columns
for feature in ['MSSubClass','OverallQual','OverallCond']:
    raw_data[feature] = raw_data[feature].astype('object')


# **Let us now recheck the data type once again after we have done the conversion in the immediate last step**

# In[7]:


# recheck of the data type
raw_data.dtypes


# <a id='Feature_Engineering'></a>
# ## 3.2 Feature Engineering
# 
# 
# 

# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="key.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                     <b> Features like 'YearBuilt' and 'YearRemodAdd' represent the initial construction year and year of remodeling respectively. Create new columns namely, 'Buiding_age' and 'Remodel_age' that provide the information about the age of building and years since remodeled
#           <br>
#                     </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# In[8]:


# 'now().year' gives the current year
# store the year as 'current_year'
current_year = int(dt.datetime.now().year)          


# In[9]:


# creating 2 new columns as 'Buiding_age' and 'Remoel_age' 
Buiding_age = current_year - raw_data.YearBuilt
Remodel_age = current_year - raw_data.YearRemodAdd


# In[10]:


# add the above columns in our dataframe
raw_data['Buiding_age'] = Buiding_age
raw_data['Remodel_age'] = Remodel_age


# In[11]:


# printing the head of the data to check whether the new columns are added or not
raw_data.head()


# In[12]:


raw_data.shape


# **We see the dataframe has 82 columns and 1460 observations**

# <a id='Missing_Data_Treatment'></a>
# ## 3.3. Missing Data Treatment
# We can not perform the matrix operations in PCA without removing null values in the data 

# **First run a check for the presence of missing values and their percentage for each column. Then choose the right approach to remove them**

# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="key.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                     <b>In order to get the count of missing values in each column, we use the in-built function .isnull().sum()
#                     </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# In[13]:


# sorting variables on the basis of null values
# 'ascending = False' sorts values in the descending order
Total = raw_data.isnull().sum().sort_values(ascending=False)          

# percentage of missing values
Percent = (raw_data.isnull().sum()*100/raw_data.isnull().count()).sort_values(ascending=False)   

# concat the 'Total' and 'Percent' columns using 'concat' function
# 'keys' is the list of column names
# 'axis = 1' concats along the columns
missing_data = pd.concat([Total, Percent], axis=1, keys=['Total', 'Percent'])    
missing_data


# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="note.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
# <b>The variables 'PoolQC', 'MiscFeature', 'Alley', etc. have a higher percentage of missing values. So maybe removing these variables will be a good option<br><br>
# 
# But, there is a catch here!<br><br>
# 
# According to the data definition, for the variable 'Alley', 'NA' is the type of alley access. But, Python treats this 'NA' as a null value. <br>
# 
# Check for such false missing values and replace them with their actual meaning</b>     </font>
#             </div>
#         </td>
#     </tr>
# </table>

# **Replace the 'NA' values with their actual meaning as per the data definition**

# In[14]:


# replace NA values in 'Alley' with a valid value, 'No alley access' 
raw_data['Alley'].fillna('No alley access' , inplace = True)


# In[15]:


# 'MasVnrType' have 0.55% NA values, replace it with 'None'
raw_data['MasVnrType'].fillna('None' , inplace = True)


# In[16]:


# use 'for' loop for filling NA values with 'No Basement' in the following 5 columns 
for col in ['BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinType2']:
    raw_data[col].fillna('No Basement' , inplace = True)


# In[17]:


# replace NA values in 'Electrical' with its mode 'SBrkr'
raw_data['Electrical'].fillna('SBrkr' , inplace = True)


# In[18]:


# replace null values in 'FireplaceQu' with a valid value, 'No Fireplace' 
raw_data['FireplaceQu'].fillna('No Fireplace' , inplace = True)


# In[19]:


# use 'for loop' to replace NA values in the below columns with a valid value, 'No Garage' 
for col in ['GarageType','GarageFinish','GarageQual','GarageCond']:
    raw_data[col].fillna('No Garage' , inplace = True)


# In[20]:


# replace NA values in 'PoolQC' with a valid value, 'No Pool'
raw_data['PoolQC'].fillna('No Pool' , inplace = True)


# In[21]:


# replace NA values in 'Fence' with a valid value, 'No Fence'
raw_data['Fence'].fillna('No Fence' , inplace = True)


# In[22]:


# replace NA values in 'MiscFeature' with a valid value, 'None'
raw_data['MiscFeature'].fillna('None' , inplace = True)


# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="note.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>For the numerical variables, replace the missing values by their respective mean, median or mode as per the requirement </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# In[23]:


# 'LotFrontage' has 17.74% of missing values, Replace these with its median value
raw_data['LotFrontage'].fillna(raw_data['LotFrontage'].median() , inplace = True)


# In[24]:


# 'MasVnrArea' have 0.55% missing values, replace it with its mode 0
raw_data['MasVnrArea'].fillna(0 , inplace = True)


# In[25]:


# replace missing values in 'GarageYrBlt' with its mode 0
raw_data['GarageYrBlt'].fillna(0 , inplace = True)


# **After replacing the null values, check for the null values for the final time**

# In[26]:


# any().sum() gives the total number of columns with null values
raw_data.isnull().any().sum()  


# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="note.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b> The above output shows that there are no missing values in the data</b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# <a id="CPCS"> </a>
# ## 4. Compute Principal Components (from scratch)

# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="key.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                     <b>Perform PCA with the following steps:<br><br>
#                         1. Filter the numerical variables <br>
#                         2. Scale the data to get variables on the same scale
# <br>
#                         3. Compute covariance matrix<br>
#                         4. Calculate eigenvalues and eigenvectors of the covariance matrix<br>
#                         5. Decide the number of principal components<br>
#                         6. Obtain principal components
#                 </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# <a id='Data_Prepare'></a>
# ### 4.1 Prepare the Data 
# 
# Separate the numerical variables, as we will perform PCA on the numerical data
# 

# In[27]:


# select the numerical variables and store it as 'df_numeric_features'
df_numeric_features = raw_data.select_dtypes(include=[np.number])

# to select all the 'numerical' features(independent variables), drop target variable from 'df_numeric_features' 
# use 'drop' function to drop the entire column
df_num = df_numeric_features.drop('SalePrice',axis=1)       

# head() to display top five rows
df_num.head()


# <a id='Scale'></a>
# ### 4.2 Scale the Data
# The variables like 'YearBuilt', 'MasVnrArea', 'OpenPorchSF', etc. have a different value range. We scale the variable to get all the variables in the same range. With this, we can avoid a problem in which some features come to dominate solely because they tend to have larger values than others
# 

# In[28]:


# fit_transform() transforms the data by first computing the mean and sd and later scaling the data
df_num_std = StandardScaler().fit_transform(df_num)

print(df_num_std)


# In[29]:


# 'shape' function gives the total number of rows and columns in the scaled data
print(df_num_std.shape)


# **Use these 35 standardized variables to find the principal components**

# <a id='cov_mat'></a>
# ### 4.3 Covariance Matrix
# 
# PCA aims to minimize the distortions and to summarize the essential information in the data. These distortions (noise, redundancy, etc.) reflect in the off-diagonal values of the covariance matrix

# In[30]:


# generate the covariance matrix using 'cov' function
cov_mat = np.cov(df_num_std.T)

# as 'cov_mat' is a numpy array, select first five observations with [0:5]
print(cov_mat[0:5])


# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="note.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b> The covariance matrix is a square matrix consists of covariance between 35 variables </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# <a id='eigen'></a>
# ### 4.4 Compute Eigenvalues and Eigenvectors 
# 

# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="key.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>Eigenvalues: The diagonal values of the diagonalized covariance matrix are called eigenvalues of the covariance matrix. Large eigenvalues correspond to large variances<br><br>
#                         
# Eigenvectors: The eigenvectors give directions of the new rotated axes 
#                      </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[31]:


# use 'eig' function to compute eigenvalues and eigenvectors of the covariance matrix
eig_val, eig_vec = np.linalg.eig(cov_mat)

print('Eigenvalues:','\n','\n', eig_val,"\n")

print('Eigenvectors:','\n','\n',eig_vec,'\n')


# <a id='components'></a>
# ### 4.5 Decide Number of Principal Components

# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="key.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>There are two ways to decide the number of principal components<br><br>
# 1) eigenvalue-one criteria: Select the components that have eigenvalues greater than 1<br>
# 2) Choose the number of components before the elbow point of the scree plot</b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[32]:


# create a list of eigenvalues
eig_val = list(eig_val)

# 'sort(reverse = True)' will sort the eigenvalues in the descending order

eig_val.sort(reverse = True)
print(eig_val)


# **Now let us use the scree plot to decide the number of components**

# #### Scree plot: Plot the eigenvalues and choose the components before elbow point 

# In[33]:


# 'bp' represents blue color and pentagonal shape of points
plt.plot(eig_val,'bp')            

# plot a line plot
plt.plot(eig_val) 

# label the x-axis
plt.xlabel('Principal Components')    

# label the y-axis
plt.ylabel('Percentage of explained variance')      

# use 'annonate' function to draw an arrow between points xy and xytext
# 's' is a argument to write text
# we can change the facecolor and arrowstyle; this is only for representation purpose
plt.annotate(text ='Elbow Point', xy=(4,1.5), xytext=(5, 2.5), arrowprops=dict(facecolor='black', arrowstyle = 'simple'))

# title of the plot
plt.title('Scree Plot')

plt.show()   


# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="note.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>It can be observed that, after the elbow point, principal components do not contribute much to the variance in the data. That means, we can choose eigenvectors corresponding to first five eigenvalues as principal components
#                        </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# <a id='pca'></a>
# ### 4.6 Calculate Principal Components 
# 

# In[34]:


eigenvector = eig_vec[:,0:5]

eigenvector


# **Generate a new dataset of reduced dimensions by multiplying standardize data and set of eigenvectors**

# In[35]:


# take the dot product of 'df_num_std' with 'eigenvector' to obtain new dataset
# create a dataframe of principal components
df_pca = pd.DataFrame(df_num_std.dot(eigenvector), columns= ['PC1','PC2','PC3','PC4','PC5'])

# head() to display top five rows
df_pca.head()


# In[36]:


# checking shape of new data
df_pca.shape


# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="note.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>In the above output, we obtained the data with reduced dimensions. The new dataset has 1460 observations and 5 columns, i.e. we have decreased the number of numerical features from 35 to 5</b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# **Now, we will use the in-built python function from sci-kit learn library to compute principal components**

# <a id='pcafunction'></a>
# ## 5. PCA using sklearn 
# 

# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="key.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>Use the in-built PCA function from the sklearn library to perform PCA and check the results with the obtained data with reduced dimensions (using scratch method)
#                 </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# In[37]:


# specify required no of components
# take 'n_components=5' based on the analysis of scree plot
pca = PCA(n_components=5, random_state=0)  

# fit_transform() computes the principal components 
# pass the standardized data to fit PCA
PrincipalComponents = pca.fit_transform(df_num_std)


# In[38]:


# create a dataframe of principal components
PCA_df = pd.DataFrame(data = PrincipalComponents, columns = ['PC1', 'PC2','PC3','PC4','PC5'])

# head() to display top five rows
PCA_df.head()


# **Here, we have used the in-built PCA function to perform dimension reduction and obtained the new dataset with 5 dimensions**

# <table align="left">
#     <tr>
#         <td width="8%">
#             <img src="note.png">
#         </td>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b> The signs of the first four principal components are reversed in the output obtained from the in-built function, as compared to the results obtained from scratch.<br><br>
# The signs depend on how the algorithm solves the eigenvector problem underlying the PCA operation. The scratch method is using the eigendecomposition method to compute eigenvalues and eigenvectors; while in-built function uses the SVD method.<br>
# The difference in the signs does not affect the variances explained by the principal components. Let, PC1 be the component of maximum variation. If we consider -(PC1) instead of PC1, then also we will obtain the same variance in the data</b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# <a id='Conclusion'></a>
# ## 6. Conclusion 

# We have performed the PCA technique using the in-built function as well as from scratch and have reduced the dimension of the numerical variables from 35 to 5. The obtained principal components explains most of the variance in the data without losing much information.

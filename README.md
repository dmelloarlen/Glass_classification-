# Glass Classification Report

## Data Cleaning

**Handled by:** Jenil Mistry

### Process Overview:

1. **Check for Null Values:**
   - **Action:** Inspected the dataset for any null values.
   - **Result:** No null values were found in the dataset.

2. **Check for Duplicates:**
   - **Action:** Identified and removed duplicate entries.
   - **Result:** Found and removed 1 duplicate record.

3. **Data Type Conversion:**
   - **Action:** Converted all columns from `float64` to `int64` using the `astype` function.
   - **Result:** All columns successfully converted to `int64`.

## Data Analysis

### Steps:

1. **Reading the Data:**
   - Loaded the cleaned data into the analysis environment.

2. **Statistical Analysis:**
   - **Min/Max Calculation:**
     - Utilized the `min` and `max` functions to determine the minimum and maximum values of the quality attribute.

## Data Representation

### Tools Used:

- **Libraries:** Streamlit, Matplotlib

### Features:

1. **Interactive Graph Selection:**
   - **Implemented Using:** Streamlit's `selectbox` function.
   - **Purpose:** Allows users to select the column and type of graph they want to visualize.

2. **Graph Types Available:**
   - **Streamlit:**
     - **Bar Graph:** `bar_chart`
     - **Line Graph:** `line_chart`
     - **Scatter Chart:** `scatter_chart`
   - **Matplotlib:**
     - **Bar Graph:** `bar`
     - **Line Graph:** `line`
     - **Scatter Chart:** `scatter`

3. **Download Feature:**
   - **Implemented Using:** File handling and `read byte` method.
   - **Purpose:** Allows users to download the graphs using Streamlit's `download_button`.

### Summary:

The data cleaning process ensured the integrity of the dataset by handling duplicates and converting data types appropriately. The analysis provided insights into the range of quality values. Finally, data representation tools in Streamlit and Matplotlib offered a user-friendly way to visualize and download the data, enhancing the accessibility and usability of the analysis.





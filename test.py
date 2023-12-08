#for mat_position in range(126,236):
count = 0  # Start Count
Material = []  # Material Name
Check_already = set()  # Material Name Before Check

for i in range(len(data_3d)):
    part_before = data_3d[i][1]  # All Of Project
    r = 0
    
    while r < len(part_before):
        # (Delete) if NaN
        print(part_before[r])
        if is_nan_or_none(part_before[r]) and not isinstance(part_before[r], str):
            r += 1  # Move to the next element
            continue

        # skip
        elif part_before[r] in Check_already or part_before[r] is None:
            r += 1  # Move to the next element
            continue

        # (Select) New information
        else:
            Material.append(part_before[r])
            Check_already.add(part_before[r])
            count_mat_already[part_before[r]] = 1
            r += 1  # Move to the next element

matName = "DC Cable -1Cx6 Sq.mm, (PV Module to DC Box to Inverter)"#ชื่อที่จะหา
print(f"============= Material Count  ============================")
print(matName)
print(f"Lens : {len(Material)}")
print(f"============= Parts  ============================")
part_before = []
Material = []
qty = []
name_plot = []
watt_plot = []
data_plot = []
date_plot = []
for i in range(len(data_3d)):
    part_before = data_3d[i][1]  # All Of Project
    Material = data_3d[i][3]  # All Of Project

    if matName in part_before:
        position = part_before.index(matName)
        data_plot.append(Material[position])
        date_plot.append(data_3d[i][2][position])
        name_plot.append(data_3d[i][0][0])
        watt_plot.append(data_3d[i][6][0])
        print(f"{i+1}")
        print(data_3d[i][0])
        print(f"Material - {data_3d[i][1][position]}")
        print(data_3d[i][3][0])
        print(data_3d[i][5])
        print("----------------------------------")
    else:
        continue

#---------- Mat Plot()
y_values = data_plot
x_values = date_plot
#---------- Mat Plot()
# x_values = matCost[0]
# y_values = [date_value] * len(matCost[0])
print("Lens Project ================================")
print(len(data_3d))
# print(data_3d)

print("Data ข้อมูล ================================")
print(x_values)
print("Date เวลา  ================================")
print(y_values)


print("Lens ================================")
print(f"Data Len : {len(x_values)}")
print(f"Date Len : {len(y_values)}")
print(f"Name Len : {len(name_plot)}")
print(f"Watt Len : {len(watt_plot)}")

# Create a DataFrame with the specified columns
df = pd.DataFrame({
    'Qty': date_plot,
    # 'Project': watt_plot,
    'Mat_Cost': data_plot,
    'Watt': watt_plot,
})

name_title = f"{matName} - Scatterplot"



# Sample data
x_data = date_plot
y_data = data_plot
name_plotly = name_plot

name_title = f"Scatter Plot - BOQ {matName}";

# Generate random data for demonstration
np.random.seed(42)

# Sample data
# date_plot = np.random.rand(100)
# data_plot = np.random.rand(100)
# watt_plot = np.random.rand(100)
# name_plotly = np.random.choice(['Project_A', 'Project_B', 'Project_C'], size=100)

# Create a DataFrame with the specified columns
df = pd.DataFrame({
    'Qty': date_plot,
    'Project': name_plotly,
    'Mat_Cost': data_plot,
    'Watt': watt_plot,
})

# Set the number of bins to 20 for all histograms
bins_dict = {col: 20 for col in df.columns}

# Create Scatterplot Matrix using plotly.figure_factory
figure = ff.create_scatterplotmatrix(
    df,
    diag='histogram',
    index='Project',
    colormap='Blues',
    height=800,
    colormap_type='seq',
    width=1000,
    # hist_n_bins=bins_dict,
)

# Show the plot
figure.show()

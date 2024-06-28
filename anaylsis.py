import pandas as pd
import streamlit as sl
import matplotlib.pyplot as plt
try:
    df= pd.read_csv("glass_clean.csv")
    print(df)
    class Ana:
        def info():
            sl.subheader("Attribute Information")

            sl.write("Id number: 1 to 214")
            sl.write("RI: refractive index")
            sl.write("Na: Sodium (unit measurement: weight percent in corresponding oxideare attributes 4-10")
            sl.write("Mg: Magnesium")
            sl.write("Al: Aluminum")
            sl.write("Si: Silicon")
            sl.write("K: Potassium")
            sl.write("Ca: Calcium")
            sl.write("Ba: Barium")
            sl.write("Fe: Iron")

            sl.subheader("Type Colum specification ")
            sl.write("1 building_windows_float_processed")
            sl.write("2 building_windows")
            sl.write("3 vehicle_windows")
            sl.write("4 vehicle_windows")
            sl.write("5 containers")
            sl.write("6 tableware")
            sl.write("7 headlamps")
            sl.subheader("Glass classification ")
            # sl.write(df)
            print(df.info())
            # name=df.columns
            sl.write(df)
            df.sort_values(df.columns[-9],axis=0,ascending=[False],inplace=True)
            sl.write("glass with minimum quality:",df.tail(1))
            sl.write("glass with maximum quality:",df.head(1))
            # num = ['1', '2', '3', '4', '5', '6', '7'] 
       
        def plot():
            a=sl.selectbox("choose one",df.columns,index=2)
            al=["line_graph","Bar_chart","scatter"]
            a1=sl.selectbox("choose one",al,index=1)
            
            if a1=="line_graph":
                sl.line_chart(df[a])
                plt.plot(df["Unnamed: 0"],df[a] )
                sl.pyplot(plt)
                plt.show()
                plt.savefig("line.png")

                a= plt.savefig("line.png")
                fig_path = "line.png"
                plt.savefig(fig_path)
                
                with open(fig_path, "rb") as file:
                    btn = sl.download_button(
                        label="Click here to download the graph",           
                        data=file,
                        file_name="line.png",
                        mime="image/png"
                )
                
            
            elif a1=="Bar_chart":
                sl.bar_chart(df[a])
                plt.bar(df["Unnamed: 0"],df[a] )
                sl.pyplot(plt)
                plt.show()
                plt.savefig("bar.png")
                
                fig_path = "bar.png"
                plt.savefig(fig_path)
                
                with open(fig_path, "rb") as file:
                    btn = sl.download_button(
                        label="Click here to download the graph",
                        data=file,
                        file_name="bar.png",
                        mime="image/png"
                    )
                
            elif a1=="scatter":
                sl.write("scatter chart")
                plt.scatter(df["Unnamed: 0"],df[a] )
                sl.pyplot(plt)
                plt.show()
                fig_path = "Scatter.png"
                plt.savefig(fig_path)
            
                with open(fig_path, "rb") as file:
                    btn = sl.download_button(
                        label="Click here to download the graph",
                        data=file,
                        file_name="Scatter.png",
                        mime="image/png"
                    )
                sl.scatter_chart(df[a])
            else:
                sl.write("Pls select apporopriate chart")
            # sl.download_button("download for downloading it in csv",data=df[a].to_csv(),file_name="graph.csv")
        
except Exception as e:
        sl.write(e)

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
            sl.download_button("download for downloading it in csv",data=df[a].to_csv(),file_name="graph.csv")
        def home():
            

            # Title
            sl.title("Glass Classification Overview")

            # Introduction
            sl.header("Introduction")
            sl.write("""
            Glass classification is the process of categorizing different types of glass based on their chemical composition and physical properties. This classification has applications in various domains, including forensics, recycling, and manufacturing.
            """)

            # Types of Glass
            sl.header("Types of Glass")
            sl.write("""
            Glass can be broadly classified into several categories, each with specific characteristics and uses:

            - **Soda-lime Glass**: The most common type, used in windows and bottles. It contains silica, soda, and lime.
            - **Lead Glass**: Known for its clarity and brilliance, used in decorative items and radiation shielding.
            - **Borosilicate Glass**: Resistant to thermal shock, used in laboratory glassware and cookware.
            - **Aluminosilicate Glass**: High-strength glass used in electronic displays and industrial applications.
            - **Specialty Glass**: Includes various other types like colored glass, fiber glass, and laminated glass, tailored for specific uses.
            """)

            # Properties Used for Classification
            sl.header("Properties Used for Classification")
            sl.write("""
            The classification of glass is often based on its chemical composition and physical properties:

            - **Chemical Composition**: The presence and proportion of elements like Silicon (Si), Sodium (Na), Calcium (Ca), Magnesium (Mg), Aluminum (Al), Potassium (K), Barium (Ba), and Iron (Fe).
            - **Physical Properties**: Such as refractive index, density, and thermal expansion coefficient.
            """)

            # Applications of Glass Classification
            sl.header("Applications of Glass Classification")
            sl.write("""
            1. **Forensic Science**:
            - **Crime Scene Investigation**: Glass fragments can be analyzed to determine their source, linking them to potential locations or objects at a crime scene.
            - **Comparison of Samples**: Forensic experts compare the refractive index and elemental composition of glass samples to establish connections between crime scenes and suspects.

            2. **Recycling**:
            - **Separation of Glass Types**: Different types of glass are separated during recycling processes to ensure effective reuse and to avoid contamination.
            - **Identification of Contaminants**: Proper classification helps in identifying contaminants in recycled glass batches.

            3. **Manufacturing**:
            - **Quality Control**: Ensuring consistency in the composition and properties of glass used in various products.
            - **Development of New Materials**: Tailoring the composition of glass to develop new materials with desired properties, such as increased strength or thermal resistance.
            """)

            # Techniques for Glass Classification
            sl.header("Techniques for Glass Classification")
            sl.write("""
            1. **Chemical Analysis**:
            - **Spectroscopy**: Methods like X-ray fluorescence (XRF) and Inductively Coupled Plasma Mass Spectrometry (ICP-MS) to determine the elemental composition of glass samples.
            - **Wet Chemical Analysis**: Traditional chemical methods to analyze glass composition.

            2. **Physical Analysis**:
            - **Refractive Index Measurement**: Using methods like oil immersion and automated refractometry to measure the refractive index of glass.
            - **Density Measurement**: Determining the density of glass using flotation or pycnometry.

            3. **Advanced Techniques**:
            - **Electron Microprobe Analysis**: For detailed compositional analysis at microscopic scales.
            - **Laser Ablation**: Coupled with mass spectrometry for precise compositional mapping.
            """)

            # Challenges in Glass Classification
            sl.header("Challenges in Glass Classification")
            sl.write("""
            1. **Fragmented Samples**: Especially in forensic contexts, glass fragments can be very small and difficult to analyze accurately.
            2. **Overlapping Compositions**: Different glass types may have similar compositions, making differentiation challenging without advanced techniques.
            3. **Contamination**: Presence of surface contaminants can affect the accuracy of chemical analysis.
            """)

            # Evolution and Future Directions
            sl.header("Evolution and Future Directions")
            sl.write("""
            - **Digital Forensics**: Integration of machine learning and AI to analyze glass data for classification and pattern recognition.
            - **Nanotechnology**: Development of nanoscale glass materials with unique properties for advanced applications.
            - **Sustainability**: Focus on developing environmentally friendly glass materials and recycling processes.
            """)

            # Use Cases in Detail
            sl.header("Use Cases in Detail")

            sl.subheader("Forensic Applications")
            sl.write("""
            - **Linking Evidence**: Glass fragments at a crime scene can be matched to a source, such as a broken window or bottle, providing crucial evidence.
            - **Court Admissibility**: Techniques for glass analysis must meet rigorous standards to be admissible in court, requiring precise and reliable methods.
            """)

            sl.subheader("Recycling Processes")
            sl.write("""
            - **Automated Sorting**: Modern recycling plants use automated systems to sort glass by color and type, ensuring high-quality recycling outputs.
            - **Reducing Waste**: Effective classification reduces contamination in recycled glass, increasing the efficiency and effectiveness of recycling programs.
            """)

            sl.subheader("Manufacturing and Quality Control")
            sl.write("""
            - **Consistent Production**: Manufacturers use classification to ensure consistent production of glass with desired properties for different applications.
            - **Innovative Materials**: Classification helps in developing new glass materials with enhanced properties for specific industrial uses.
            """)

            # Summary
            sl.header("Summary")
            sl.write("""
            Glass classification is a multidisciplinary field that involves identifying and categorizing glass based on its chemical and physical properties. It plays a critical role in forensic science, recycling, and manufacturing. Techniques range from traditional chemical analysis to advanced spectroscopic methods, with ongoing developments aimed at improving accuracy and efficiency.
            """)

except Exception as e:
        sl.write(e)

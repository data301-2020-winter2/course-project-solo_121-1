def load_and_process(url_or_path_to_csv_file):
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns ={"bmi": "BMI"})
        .dropna()
     )
    
    return df
load_and_process("Medical_Cost.csv")

#1
import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set_theme(style="darkgrid")
G1 = sns.countplot(x="age",hue="smoker", data=MedDataSet)

#2
import seaborn as sns
sns.set(rc={'figure.figsize':(20,15)})
sns.set_theme(style="darkgrid")
G2 = sns.jointplot(y="charges",x = "region",data=MedDataSet)

#3/RQ1
import seaborn as sns
sns.set(rc={'figure.figsize':(20,15)})
sns.set_theme(style="darkgrid")
G3 = sns.jointplot(x = "age",y="charges",hue="smoker",data = MedDataSet)

#4
import seaborn as sns
sns.set(rc={'figure.figsize':(20,15)})
sns.set_theme(style="darkgrid")
G3 = sns.jointplot(x = "bmi",y="charges",hue="region",data = MedDataSet)

#5
import seaborn as sns
sns.set(rc={'figure.figsize':(30,25)})
sns.set_theme(style="darkgrid")
#G3.set(ylim=(0,20))
G3 = sns.jointplot(x = "bmi",y="charges",hue="smoker",data = MedDataSet)

#6
import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.25)})
sns.set_theme(style="darkgrid")
#G3.set(ylim=(0,20))
G3 = sns.jointplot(x = "age",y="charges",hue="sex",data = MedDataSet)

#7
import seaborn as sns
sns.set(rc={'figure.figsize':(20,15)})
sns.set_theme(style="darkgrid")
G3 = sns.jointplot(x = "children",y="charges",hue="region",data = MedDataSet)
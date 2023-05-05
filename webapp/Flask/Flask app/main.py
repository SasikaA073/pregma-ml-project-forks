from datetime import datetime
import pandas as pd 
import pprint
from flask import Flask, render_template, request

# Open the csv file
results_df = pd.read_csv("dataset.csv")

# Define Flask application
app = Flask(__name__)

# Define functions 
def _search(dataframe:pd.DataFrame or pd.Series,column:str,keyword1:str,keyword2:str=None)->list:
    l = []
    l2 = []
    try:
        keyword1 = keyword1.lower()
        keyword2 = keyword2.lower()
        x = dataframe[column]
        len_x = x.count()
        for i in range(len_x):
            q1 = x.iloc[i].lower()
            # print(q1)
            if keyword1 in q1:
                l.append((i,q1))
    except:
        
        x = dataframe[column]
        len_x = x.count()
        for i in range(len_x):
            q1 = str(x.iloc[i])
            # print(q1)
            if keyword1 in q1:
                l.append((i,q1))
    # print(keyword1,keyword2)

    if keyword2 == None:
        return l
    else:
        try:
            keyword2 = keyword2.lower()
        except AttributeError:
            pass
        for k,v in l:
            
            q2 = v
            if keyword2 in q2:
                l2.append((k,q2))
        
        return l2     

def get_details(dataframe:pd.Series or pd.DataFrame,index:int,column_names:list=None)->list or pd.Series.core.series.Series :
    
    if column_names == None:
        return dataframe.iloc[index,:]
    else:
        l = []
        for column in column_names:
            value = dataframe.iloc[index,:][column]
            l.append(value)
        return l
    
def get_search_result(df:pd.DataFrame, column:str, keyword_1:str, keyword_2:str = None, search_result_index=0):

    r = _search(df, column, keyword_1,keyword_2)
    width = 16
    result_index_list = []

    for i , data in enumerate(r):
        result_index_list.append(f'{i} : index : {data[0]} : full_name : {data[1]}')
    
    try:
        df_index = r[search_result_index][0]
        details_series = get_details(df,index=df_index)
    
        return result_index_list, get_details(df,index=df_index)

    except IndexError:
        print("Search result not found!\n\t keyword1 =",str(keyword_1).center(width,' ') ,"; keyword2 =",str(keyword_2).center(width,' '))
        return None
        
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the input for names

                # Get the input for names
        name = request.form.get('keywords')
        if name is None:
            return "Name input is missing."



        print("\n\n"+name )
        [keyword_1, keyword_2] = name.split()

        # Function to initialize search
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Write the keyword to the log file 
        with open('log.txt', 'a') as f:
            f.write(f'{timestamp} : {name}\n')

        r = index_list, result_sheet =  get_search_result(results_df, 'full_name', keyword_1, keyword_2,)
        # data = r
        print("\n\n",r)
        return render_template("result.html", result=r) # r can be None too. if no results found
        
    else:
        return render_template("index.html")

if __name__ == "__main__":

    app.run(debug=True)
    # search()

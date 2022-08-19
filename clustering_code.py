import pre_processing
from sklearn.cluster import KMeans
import pre_processing

def Clustered_final_df(df):
    df['cluster_Id']=None

 #modify the n_clusters value to get 
    kmeans=KMeans(n_clusters=20)

    features=df[['P_Genre','S_Genre','T_Genre']]
    kmeans.fit(features)
    df['cluster_Id']=kmeans.predict(features)
    return df

def cluster_everything(input_movie):
    df=pre_processing.pre_process_all()
    df=Clustered_final_df(df)
    #2print(df)
    df.to_csv('Dataset_to_plot.csv')
    #chcek if the movie is present or not
    input_movie=input_movie.lower()
    try:
        movie_not_found=df.loc[~df['movie'].str.contains(input_movie)]
        if len(movie_not_found)==0:
            print('Movie not found')
            return 0
        get_cluster=df['cluster_Id'].loc[df['movie']].str.contains(input_movie).values[0]
        similar_movies_list=df['movie'].loc[df['cluster_Id']==get_cluster].values
        return similar_movies_list

    except:
         print('Movie not found')
    return 0



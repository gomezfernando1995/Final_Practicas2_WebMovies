import requests
import json

# URL DE TRENDING : https://api.themoviedb.org/3/trending/all/day?api_key=<<api_key>>
# URL DE PELICULAS CONTRETAS :https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US 

#!Constantes !# 
KEY='?api_key=67cfd04f6f82ac9174c13465962409c8'
LENG = '&language=es-ES'
TIME = 'week'  # tambien puede ser day 

###### OBTENER ID DE PELICULA #####
def getMovie_id(movie):
    return movie['id']

###### OBTENER TITULO DE PELICULA #####
def getMovie_title(movie):
    return movie['title']

###### MUESTRA PELICULAS DE UNA LISTA DE JSON DISCRIMINADO SEGUN SE REQUIERA ####### 
def showMovies(movies_json):

    for movie in movies_json:
        title= getMovie_title(movie)
        id = getMovie_id(movie)
        print(title,id)

###### COMPARAR 2 TITULOS Y OBTENER LINK ####### 
def isEquals (title,str):
    if title == str : return True;  return False
       

def getSpecificMovie(movies_json,selectedMovie):

    for movie in movies_json:
        title= getMovie_title(movie)
        id = getMovie_id(movie)
        if isEquals(title,selectedMovie):return url_movie+str(id)+KEY+LENG;return False
                     
###########################################################################################



page ='&page=1'
url_trending= 'https://api.themoviedb.org/3/trending/movie/'+TIME+KEY+page
url_movie= 'https://api.themoviedb.org/3/movie/'
poster_url= 'https://image.tmdb.org/t/p/w500/'

response=requests.get(url_trending)   #---Solicitamos toda la informacion con el endpoint de trending.
                                      # txt_response=r.text         ---RESPUESTA EN FORMATO TEXTO--  
res_json = response.json()            #---RESPUESTA EN FORMATO JSON-- Tranformamos en json para manejar la informacion obtenida.
movies_json = res_json['results']          # Con el datos en json podemos ingresar a la lista de resultados

url_movie_specific = getSpecificMovie(movies_json,"Black Panther: Wakanda Forever")
showMovies(movies_json)
print(url_movie_specific)



     ##['poster_path']
    
       #for movie in movies_json:
            #  title= movie['title']
            #  id = movie['id']
             # if  request.form['search']== title:
             #  url_movie_complete=url_movie+str(id)+KEY+LENG



              #<div class="row row-col-1 row-cols-sm-1 row-cols-md-2 row-cols-lg-4 mt-3">
               #     {% for movie in movies %}
                #    <div class="col-md-2 mb-3">
                 #       <img class="poster" src="{{url_img}}{{movie['poster_path']}}" alt="" ">
                  #      <p>{{movie['original_title']}}</p>
                   #     <p>{{movie['release_date']}}</p>
                   #     <!--<p>{{movie['overview']}}</p> -->
                    #</div>
                    #{% endfor %}
            
      #      </div>
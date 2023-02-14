from flask import Flask, render_template,request
import requests

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST': 
      num = str((request.form['search']))
    else:
       num ='1'

    KEY='?api_key=67cfd04f6f82ac9174c13465962409c8'
    LENG = '&language=es-ES'
    time = 'week'  # tambien puede ser day 
    page ='&page='+num
    
    url_trending= 'https://api.themoviedb.org/3/trending/movie/'+time+KEY+page+LENG
    url_movie= 'https://api.themoviedb.org/3/movie/'
    url_poster= 'https://image.tmdb.org/t/p/w300'
    url_poster_back= 'https://image.tmdb.org/t/p/w1920_and_h800_multi_faces'
    url_populary = 'https://api.themoviedb.org/3/discover/movie'+KEY+LENG+'&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate'
    
    moviedb=requests.get(url_trending)      #---Solicitamos toda la informacion con el endpoint de trending.
    moviedb_json = moviedb.json()           #---RESPUESTA EN FORMATO JSON-- Tranformamos en json para manejar la informacion obtenida.
    movies_json = moviedb_json['results']   # Con el datos en json podemos ingresar a la lista de resultados

    moviedb_pop=requests.get(url_populary)      #---Solicitamos toda la informacion con el endpoint de trending.
    moviedb_json_pop= moviedb_pop.json()           #---RESPUESTA EN FORMATO JSON-- Tranformamos en json para manejar la informacion obtenida.
    movies_json_pop = moviedb_json_pop['results']   # Con el datos en json podemos ingresar a la lista de resultados
    video = '/videos'+KEY+LENG+"&append_to_response=videos"
   
    if request.method == 'GET': 
        return render_template('index.html', movies = movies_json,url_img=url_poster,leng=LENG,movie_pop=movies_json_pop,poster_back=url_poster_back,url_movie=url_movie,video=video) ##ver aca
   
    if request.form['search'] and  request.form['search'] == '1': 
         return render_template('index.html', movies = movies_json,url_img=url_poster,leng=LENG,movie_pop=movies_json_pop,poster_back=url_poster_back,url_movie=url_movie,video=video) ##ver aca
    else:
         return render_template('index.html', movies = movies_json,url_img=url_poster,leng=LENG) ##ver aca
       #return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
     app.run(debug=True, port=4000 )




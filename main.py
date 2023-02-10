from flask import Flask, render_template,request
import requests

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    KEY='?api_key=67cfd04f6f82ac9174c13465962409c8'
    LENG = '&language=es-ES'
    time = 'week'  # tambien puede ser day 
    page ='&page=1'
  
    url_trending= 'https://api.themoviedb.org/3/trending/movie/'+time+KEY+page+LENG
    url_movie= 'https://api.themoviedb.org/3/movie/'
    url_poster= 'https://image.tmdb.org/t/p/w300'
    
    moviedb=requests.get(url_trending)      #---Solicitamos toda la informacion con el endpoint de trending.
    moviedb_json = moviedb.json()           #---RESPUESTA EN FORMATO JSON-- Tranformamos en json para manejar la informacion obtenida.
    movies_json = moviedb_json['results']   # Con el datos en json podemos ingresar a la lista de resultados
    
    if request.method == 'GET': 
        return render_template('index2.html', movies = movies_json,url_img=url_poster,leng=LENG) ##ver aca
    if request.form['search']:      
         return render_template('page_unique.html',movies = movies_json,title=request.form['search'],url_img=url_poster,leng=LENG)
    else:
        return render_template('index2.html')
      

if __name__ == '__main__':
     app.run(debug=True, port=4000 )
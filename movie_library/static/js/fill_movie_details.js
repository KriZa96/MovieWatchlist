const buttons = document.getElementById('buttons');
const cast = document.getElementById('movie-cast');
const tags = document.getElementById('movie-tags');
const description = document.getElementById('movie-description');
const movieTrailer = document.getElementById("movie-video_link")
const apiKey = '9cf43f07825083878030a29d1919039b';


function fillCast(data) {
  const actors = data.Actors.replace(/, /g, "\n");
  return actors;
}


function fillTags(data){
  const tags = data.Genre.replace(/, /g, "\n");
  return tags;
}


function fillDescription(data){
  const description = data.Plot;
  return description
}


async function getMovieData() {
  const movieTitle = document.getElementById('movie-search-box').value.replace(/ /g, "+");
  const URL = `https://omdbapi.com/?t=${movieTitle}&apikey=fc1fef96`;
  const res= await fetch(URL);
  const data = await res.json();
  if (data.Response === 'True') {
      return data;
    } else {
      alert("Movie Title Is Not Correct");
    }
}


async function searchMovieTrailer(movieTitle) {
  const searchUrl = `https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&query=${encodeURIComponent(movieTitle)}`;
  const searchResponse = await fetch(searchUrl);
  const searchData = await searchResponse.json();

  if (searchData.results) {
    const movieId = searchData.results[0].id;
    const videoUrl = `https://api.themoviedb.org/3/movie/${movieId}/videos?api_key=${apiKey}`;

    const videoResponse = await fetch(videoUrl);
    const videoData = await videoResponse.json();

    let trailerKey = null
    for(let i=0; i < videoData.results.length; i+=1){
      if (videoData.results[i].name.toLowerCase().includes("trailer")){
        trailerKey = videoData.results[i].key;
        break;
      }
    }
    if (!trailerKey) {
      trailerKey = videoData.results[0].key;
    }

    return `https://www.youtube.com/watch?v=${trailerKey}`;
  } else {
    alert("Can't find movie trailer.");
  }
}


const import_button = document.createElement("button");
import_button.id = "import_button"
import_button.innerHTML = "Import Data"; // Set button text
import_button.className = "button button--form"
import_button.type = "button"
import_button.onclick = async function() {
  const data = await getMovieData();
  cast.value = fillCast(data);
  tags.value = fillTags(data);
  description.value = fillDescription(data);
  movieTrailer.value = await searchMovieTrailer(data.Title);
};

buttons.appendChild(import_button);

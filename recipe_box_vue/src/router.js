import VueRouter from 'vue-router';
import Home from './pages/Home';
import About from './pages/About';
import RecipeBox from './pages/RecipeBox';
import AddRecipe from './pages/AddRecipe';
import RecipeDetails from './pages/RecipeDetails';
import UpdateRecipe from './pages/UpdateRecipe';

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/recipebox', component: RecipeBox, name: 'RecipeBox' },
  { path: '/addrecipe', component: AddRecipe, name: 'AddRecipe' },
  {
    path: '/updaterecipe/:recipe_id',
    component: UpdateRecipe,
    name: 'UpdateRecipe'
  },
  { path: '/about', component: About, name: 'About' },
  {
    path: '/recipedetails/:recipe_id',
    component: RecipeDetails,
    name: 'RecipeDetails'
  }
];

export default new VueRouter({ routes, mode: 'history' });

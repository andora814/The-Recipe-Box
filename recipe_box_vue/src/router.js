import VueRouter from 'vue-router';
import Home from './pages/Home';
import RecipeBox from './pages/RecipeBox';
import AddRecipe from './pages/AddRecipe';
import RecipeDetails from './pages/RecipeDetails';
import Pantry from './pages/Pantry';

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/recipebox', component: RecipeBox, name: 'RecipeBox', props: true },
  { path: '/pantry', component: Pantry, name: 'Pantry' },
  { path: '/addrecipe', component: AddRecipe, name: 'AddRecipe' },
  {
    path: '/recipedetails/:recipe_id',
    component: RecipeDetails,
    name: 'RecipeDetails'
  }
];

export default new VueRouter({ routes, mode: 'history' });

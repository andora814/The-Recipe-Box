import VueRouter from 'vue-router';
import Home from './pages/Home';
// import About from './pages/About';
// import RecipeBox from './pages/RecipeBox';
// import AddRecipe from './pages/AddRecipe';

const routes = [
  { path: '/', component: Home, name: 'Home' }
  // { path: '/categories', component: RecipeBox, name: 'RecipeBox' },
  // { path: '/addrecipe', component: AddRecipe, name: 'AddRecipe' },
  // { path: '/about', component: About, name: 'About' }
];

export default new VueRouter({ routes, mode: 'history' });

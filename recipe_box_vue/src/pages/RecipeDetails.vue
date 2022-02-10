<template>
  <div class="recipe-content">
    <h3>{{ recipeDetails.title }}</h3>
    <img :src="recipeDetails.image" class="image"/>
    <div>Ready in {{ recipeDetails.ready_in_minutes }} minutes</div>
    <div>Serves {{ recipeDetails.servings }}</div>
    <div>{{ recipeDetails.summary }}</div>
    <div>Ingredient List:
        <div v-for="ingredient in recipeIngredients" :key="ingredient.id">
          {{ ingredient.quantity}} {{ingredient.unit}} of {{ ingredient.name }}
        </div>
    </div>
    <div>Instructions: {{ recipeDetails.instructions }}</div>
    <button @click="goToUpdateRecipe(recipeDetails.id)">Update Recipe</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RecipeDetails',
  data: () => ({
    recipeDetails: null,
    recipeIngredients: null
  }),
  mounted() {
    this.getRecipeDetails(this.$route.params.recipe_id)
  },
  methods: {
    async getRecipeDetails(id) {
        const res = await axios.get(`http://localhost:8000/recipes/${id}`)
        this.recipeDetails = res.data
        this.recipeIngredients = res.data.recipe_ingredients
    },
    goToUpdateRecipe() {
      console.log(this.recipeIngredients)
        // this.$router.push(`/updaterecipe/${id}`)
        }
  }
}
</script>

<style scoped>
  .image  {
    width: 500px;
    height: 250px
  }
</style>
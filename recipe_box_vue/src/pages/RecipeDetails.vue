<template>
  <div>{{ recipeDetails.title }}</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RecipeDetails',
  data: () => ({
    recipeDetails: null
  }),
  mounted() {
    this.getRecipeDetails(this.$route.params.recipe_id)
  },
  methods: {
    async getRecipeDetails(id) {
        const res = await axios.get(`http://localhost:8000/recipes/${id}`)
        this.recipeDetails = res.data
        console.log(this.recipeDetails)
    }
  }
}
</script>

<style>

</style>
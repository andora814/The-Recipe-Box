<template>
  <div class="recipe-content">
    <h3>{{ recipe_details.title }}</h3>
    <img :src="recipe_details.image" class="image"/>
    <div>Ready in {{ recipe_details.ready_in_minutes }} minutes</div>
    <div>Serves {{ recipe_details.servings }}</div>
    <div>{{ recipe_details.summary }}</div>
    <div>Ingredient List: 
      <div v-if="show_ingredients">
        <div v-for="ingredient in recipe_ingredients" :key="ingredient.id">
          {{ ingredient.quantity}} {{ingredient.unit}} of {{ ingredient.name }}
        </div>
        <button @click="editIngredientList">Edit Ingredients</button>
      </div>
      <div v-if="edit_ingredients">
        <div v-for="ingredient in recipe_ingredients" :key="ingredient.id">
          <input v-on:input="handleFormChange" :value="ingredient.quantity" /> <input v-on:input="handleFormChange" :value="ingredient.unit" /> of <input v-on:input="handleFormChange" :value="ingredient.name" />
        </div>
        <button @click="saveIngredientList">Save Ingredients</button>
      </div>
    </div>
    <div>Instructions: 
      <div v-if="show_instructions">
        {{ recipe_details.instructions }}
        <button @click="editInstructions">Edit Instructions</button>
      </div>
      <div v-if="edit_instructions">
        <input v-on:input="handleFormChange" name="new_instructions" :value="recipe_details.instructions" /> 
        <button @click="saveInstructions(recipe_details.id)">Save Instructions</button>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RecipeDetails',
  data: () => ({
    recipe_details: null,
    recipe_ingredients: null,
    show_ingredients: true,
    edit_ingredients: false,
    show_instructions: true,
    edit_instructions: false,
    new_instructions: ''
  }),
  mounted() {
    this.getRecipeDetails(this.$route.params.recipe_id)
  },
  methods: {
    async getRecipeDetails(id) {
        const res = await axios.get(`http://localhost:8000/recipes/${id}`)
        this.recipe_details = res.data
        this.recipe_ingredients = res.data.recipe_ingredients
    },
    editIngredientList() {
      this.edit_ingredients = true
      this.show_ingredients = false
    },
    saveIngredientList() {
      this.edit_ingredients = false
      this.show_ingredients = true
    },
    editInstructions() {
      this.edit_instructions = true
      this.show_instructions = false
    },
    async saveInstructions(id) {
      this.edit_instructions = false
      this.show_instructions = true
      let res = await axios.put(`http://localhost:8000/recipes/${id}`, {
                "title": this.recipe_details.title,
                "ready_in_minutes": this.recipe_details.ready_in_minutes,
                "servings": this.recipe_details.servings,
                "source_url": this.recipe_details.source_url,
                "image": this.recipe_details.image,
                "summary": this.recipe_details.summary,
                "instructions": this.new_instructions
            }, {
                auth: {
                    username: 'recipeboxuser',
                    password: 'recipe'
                }
            })
      this.recipe_details.instructions = res.data.instructions
    },
    handleFormChange(e) {
      this[e.target.name] = e.target.value
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
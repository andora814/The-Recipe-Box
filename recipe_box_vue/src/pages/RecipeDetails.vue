<template>
  <div class="recipe-content">
    <div class="image-and-title">
      <div class="title-and-ready-in-and-serves">
        <h2>{{ recipe_details.title }}</h2>
          <div><strong>Ready in </strong>{{ recipe_details.ready_in_minutes }} minutes</div>
          <div><strong>Serves </strong>{{ recipe_details.servings }}</div>
      </div>
      <img :src="recipe_details.image" class="image"/>
    </div>
    
    <div><strong>Notes: </strong>{{ recipe_details.summary }}</div>
    <div><strong>Ingredient List: </strong>
      <div v-if="show_ingredients">
        <div v-for="ingredient in recipe_ingredients" :key="ingredient.id">
          {{ ingredient.quantity}} {{ingredient.unit}} of {{ ingredient.name }}
        </div>
        <button @click="editIngredientList">Edit</button>
      </div>
      <div v-if="edit_ingredients">
        <div v-for="(ingredient, index) in recipe_ingredients" :key="ingredient.id">
          <input v-on:input="handleFormChange" :value="ingredient.quantity" v-bind:index="index" name="new_quantity"/> <input v-on:input="handleFormChange" :value="ingredient.unit" name="new_unit"/> of {{ ingredient.name }} 
          <button @click="handleEdit(ingredient.id, index)">Save</button>
        </div>
        <button @click="saveIngredientList">Save</button>
      </div>
    </div>
    <div><strong>Instructions: </strong>
      <div v-if="show_instructions">
        {{ recipe_details.instructions }}
        <button @click="editInstructions">Edit</button>
      </div>
      <div v-if="edit_instructions">
        <input v-on:input="handleFormChange" name="new_instructions" :value="recipe_details.instructions" class="new-instructions"/> 
        <button @click="saveInstructions(recipe_details.id)">Save</button>
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
    new_instructions: '',
    new_quantity: 0,
    new_unit: ''
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
      window.location.reload()
    },
    editInstructions() {
      this.edit_instructions = true
      this.show_instructions = false
    },
    async saveInstructions(recipe_id) {
      this.edit_instructions = false
      this.show_instructions = true
      let res = await axios.put(`http://localhost:8000/recipes/${recipe_id}`, {
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
      window.location.reload()
    },
    handleFormChange(e) {
      this[e.target.name] = e.target.value
    },
    async handleEdit(id, index) {
      let res = await axios.put(`http://localhost:8000/recipeingredients/${id}`, {
                "recipe_id": this.recipe_ingredients[index].recipe_id,
                "ingredient_id": this.recipe_ingredients[index].ingredient_id,
                "name": this.recipe_ingredients[index].name,
                "quantity": this.new_quantity,
                "unit": this.new_unit
      }, {
                auth: {
                    username: 'recipeboxuser',
                    password: 'recipe'
                }
            })
      this.recipe_ingredients.quantity = res.data.quantity
      this.recipe_ingredients.unit = res.data.unit
      
    }
}
}
</script>

<style scoped>
  .image  {
    height: 250px
  }
  .image-and-title {
    display: flex;
    justify-content: center;
    margin: 10px;
    justify-content: space-around;
  }
  .recipe-content {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    color: #03195a
  }
  .ready-in-and-serves {
    display: flex;
    justify-content: space-around;
  }
  .title-and-ready-in-and-serves {
    display: flex;
    flex-direction: column;
  }
  .new-instructions {
    width: 500px;
    height: 200px;
    margin: 10px; 
  }

</style>
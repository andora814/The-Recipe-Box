<template>
  <div class="recipe_container">
    <div class="container">
      <div @click="selectRecipe()">
        <h3> {{ recipe.title }} </h3>
        <img :src="recipe.image" alt="recipe picture" class="image" />
      </div>
      <div @click="deleteRecipe(recipe.id)" class="delBtn">remove</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RecipeCard',
  data: () => ({
    showName: false,
    picclass: 'normal'
  }),
  props: {
    recipe: Object
  },
  methods: {
    async deleteRecipe(id) {
        await axios.delete(`http://localhost:8000/recipes/${id}`, {
          auth: {
            username: 'recipeboxuser',
            password: 'recipe'
          }
        })
        this.$emit('handleDelete', this.recipe.id)
    },
    selectRecipe(){
      this.$emit('click')
    }
}
}
</script>

<style scoped>

.container {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.center {
  position: absolute;
  top: 50%;
  text-align: center;
  font-size: 22px;
  color: black
}

.image  {
    width: 250px;
    height: 125px
  }

.blur {
  opacity: 0.6;
}

.recipe_container {
  width: 250px;
  margin-bottom: 10px;
  background-color: green;
  border-radius: 10px;
  color: white;
  cursor: pointer;
}

.recipe_container:hover {
  transform: scale(1.025);
}

.delBtn {
  width: 100%;
  background-color: green;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
  border-radius: 0 0 7px 7px
}

.delBtn:hover {
  background-color: #f4aa09;
  color: white
}


</style>
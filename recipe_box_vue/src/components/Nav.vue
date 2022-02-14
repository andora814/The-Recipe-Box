<template>
  <nav>
    <router-link to="/" name="Home" class="nav-btn">Home</router-link>
    <router-link to="/recipebox" class="nav-btn">Recipe Box</router-link>
    <router-link to="/pantry" class="nav-btn">Pantry</router-link>
    <router-link to="/addrecipe" class="nav-btn">Add a Recipe</router-link>
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  data: () => ({
    categories: null
  })
};
</script>

<style scoped>
.nav-btn {
  cursor: pointer;
  text-decoration: none;
  color: grey;
}
.nav-btn:hover {
  color: #f4aa09;
  font-weight: bolder;
}
.nav-btn {
  color: white;
  font-size: 25px;
}
nav {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  background-color: #017754;
}

</style>

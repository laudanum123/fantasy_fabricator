import { createRouter, createWebHashHistory } from 'vue-router'
import AdventureBuilder from '../components/adventure_builder.vue'
import CampaignManager from '../components/campaign_manager.vue'
import CharacterGenerator from '../components/character_generator.vue'
import Community_Support from '../components/community_support.vue'
import Encounter_Builder from '../components/encounter_builder.vue'
import Map_Generator from '../components/map_generator.vue'
import Landing_Page from '../components/landing_page.vue'

const routes = [
  {
    path: '/',
    name: 'landing_page',
    component: Landing_Page
  },
  {
    path: '/adventure_builder',
    name: 'adventure builder',
    component: AdventureBuilder
  },
  {
    path: '/campaign_manager',
    name: 'campaign manager',
    component: CampaignManager
  },
  {
    path: '/character_generator',
    name: 'character generator',
    component: CharacterGenerator
  },
  {
    path: '/community_support',
    name: 'community support',
    component: Community_Support
  },
  {
    path: '/encounter_builder',
    name: 'encounter builder',
    component: Encounter_Builder
  },
  {
    path: '/map_generator',
    name: 'map generator',
    component: Map_Generator
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

export const state = () => ({
  addr_list: [
    {
      name: "tanino",
      birthday: "2018-03-18",
      gender: 0,
      address: "yokomaha city",
      jobs: ["会社員"],
      note: "other"
    },
    {
      name: "kenichi",
      birthday: "2011-12-31",
      gender: 1,
      address: "tokyo city",
      jobs: ["会社員"],
      note: "other 2"
    }
  ]
})

export const actions = {
  add(context, addr) {
    context.commit("add", addr)
  },
  set(context, addr) {
    context.commit("set", addr)
  },
  remove(context, index) {
    context.commit("remove", index)
  }
}

function addr_set(addr) {
  return {
    name: addr.name,
    birthday: addr.birthday,
    gender: addr.gender,
    address: addr.address,
    jobs: addr.jobs,
    note: addr.note
  }
}

import Vue from "vue"

export const mutations = {
  add(state, addr) {
    Vue.set(state.addr_list, state.addr_list.length, addr_set(addr))
  },
  remove(state, index) {
    state.addr_list.splice(index, 1)
  },
  set(state, addr) {
    Vue.set(state.addr_list, addr.index, addr_set(addr))
  }
}

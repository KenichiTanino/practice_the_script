<template>
  <div>
    <el-tabs v-model="activeName" type="border-card">
      <el-tab-pane label="service1" name="service1">
        <addr-table/>
      </el-tab-pane>
      <el-tab-pane label="service2" name="service2">
        <addr-form/>
      </el-tab-pane>
      <el-tab-pane label="service3" name="service3">
        {{ this.$store.state.tables.addr_list.length }}
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import AddrTable from "~/components/addr-table.vue"
import AddrForm from "~/components/addr-form.vue"

export default {
  components: {
    AddrTable,
    AddrForm
  },
  data() {
    return {
      activeName: "service1"
    }
  }
}
</script>

<style>
</style>

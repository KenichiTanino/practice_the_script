<template>

<el-table :data="accounts">

      <el-table-column
        prop="id"
        label="id"
        width="100">
      </el-table-column>

      <el-table-column
        prop="name"
        label="Name"
        width="280">
      </el-table-column>

      <el-table-column
        prop="email"
        label="Email"
        width="280">
        <template slot-scope="scope">
        	<el-input v-model="scope.row.email" ></el-input>
		</template>
      </el-table-column>

<el-table>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      accounts: []
    }
  },
  async asyncData() {
    const baseUrl = '/api/accounts'
    const response = await axios.get(baseUrl)
    return {
      accounts: response.data.result
    }
  }
}
</script>

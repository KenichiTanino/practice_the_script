<template>
  <div>
    <el-table
      :data="addr_list"
      style="width: 100%">
      <el-table-column
        prop="name"
        label="名前"
        width="100"/>
      <el-table-column
        prop="birthday"
        label="誕生日"
        width="100"/>
      <el-table-column
        prop="gender"
        label="性別"
        width="80">
        <template slot-scope="scope">
          {{ getGender(scope.row.gender) }}
        </template>
      </el-table-column>
      <el-table-column
        prop="address"
        label="住所"/>
      <el-table-column
        label="職業">
        <template slot-scope="scope">
          {{ scope.row.jobs.toString() }}
        </template>
      </el-table-column>
      <el-table-column
        prop="note"
        label="備考"/>
      <el-table-column width="160">
        <template slot-scope="scope">
          <el-button type="primary" size="small" @click="removeRow(scope.$index)">Remove</el-button>
          <el-button type="primary" size="small" @click="editRow(scope.row, scope.$index)">Edit</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog
      :visible="dialogVisible" title="Edit" width="70%" >
      <addr-form :row="editData" :index="listIndex" @close-dialog="close"/>  
    </el-dialog>

  </div>
</template>

<script>
import AddrForm from "~/components/addr-form.vue"

export default {
  components: {
    AddrForm
  },
  props: {
    dialogVisible: { type: Boolean, default: false }
  },
  data() {
    return {
      addr_list: this.$store.state.tables.addr_list,
      editData: {},
      listIndex: ""
    }
  },
  methods: {
    getGender(gender) {
      var genders = ["男性", "女性", "その他"]
      return genders[gender]
    },
    removeRow(index) {
      this.$store.dispatch("tables/remove", index)
    },
    editRow(row, index) {
      this.listIndex = index
      this.editData = row
      this.dialogVisible = true
    },
    close() {
      this.dialogVisible = false
    },
    update() {
      this.$confirm("This will permanently setting. Continue?", "Warning", {
        confirmButtonText: "OK",
        cancelButtonText: "Cancel",
        type: "warning"
      })
        .then(() => {
          this.$message({
            type: "success",
            message: "settings completed"
          })
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "setting canceled"
          })
        })
      return
    }
  }
}
</script>

<style>
</style>

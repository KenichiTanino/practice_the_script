<template>
  <div>
    <H1>addr form</H1>
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="名前">
        <el-input v-model="form.name"/>
      </el-form-item>
      <el-form-item label="誕生日">
        <el-date-picker v-model="form.birthday" type="date" placeholder="Pick a date" format="yyyy-MM-dd" value-format="yyyy-MM-dd" style="width: 100%;"/>
      </el-form-item>
      <el-form-item label="性別">
        <el-radio-group v-model="form.gender">
          <el-radio :label="0">男性</el-radio>
          <el-radio :label="1">女性</el-radio>
          <el-radio :label="2">その他</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="住所">
        <el-input v-model="form.address"/>
      </el-form-item>
      <el-form-item label="職業">
        <el-checkbox-group v-model="form.jobs">
          <el-checkbox label="会社員"/>
          <el-checkbox label="フリーター"/>
          <el-checkbox label="医者"/>
          <el-checkbox label="エンジニア"/>
          <el-checkbox label="その他"/>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="備考">
        <el-input v-model="form.note"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">登録</el-button>
        <el-button @click="onClose">Cancel</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
function addr_set(addr, index) {
  return {
    name: addr.name,
    birthday: addr.birthday,
    gender: addr.gender,
    address: addr.address,
    jobs: addr.jobs,
    note: addr.note,
    index: index
  }
}

export default {
  props: {
    row: { type: Object, default: undefined },
    index: { type: Number, default: undefined }
  },
  data() {
    if (this.index === undefined) {
      return {
        form: {
          name: "",
          birthday: "",
          gender: "",
          address: "",
          jobs: [],
          note: ""
        }
      }
    }
    // TODO: 範囲チェック
    var form = this.$store.state.tables.addr_list[this.index]
    return {
      form: {
        name: form.name,
        birthday: form.birthday,
        gender: form.gender,
        address: form.address,
        jobs: form.jobs,
        note: form.note
      }
    }
  },
  watch: {
    row: function(newForm) {
      this.form.name = newForm.name
      this.form.birthday = newForm.birthday
      this.form.gender = newForm.gender
      this.form.address = newForm.address
      this.form.jobs = newForm.jobs
      this.form.note = newForm.note
    }
  },
  methods: {
    onSubmit() {
      this.$confirm("This will permanently setting. Continue?", "Warning", {
        confirmButtonText: "OK",
        cancelButtonText: "Cancel",
        type: "warning"
      })
        .then(() => {
          var addr = addr_set(this.form, this.index)
          if (this.index === undefined) {
            this.$store.commit("tables/add", addr)
          } else {
            this.$store.commit("tables/set", addr)
          }
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
    },
    onClose() {
      if (this.index === undefined) {
        this.form.name = ""
        this.form.birthday = ""
        this.form.gender = ""
        this.form.address = ""
        this.form.jobs = []
        this.form.note = ""
      } else {
        this.$emit("close-dialog")
      }
    }
  }
}
</script>

<style>
</style>

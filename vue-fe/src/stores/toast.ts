import { defineStore } from "pinia";


export const useToastStore = defineStore("toast", {
    state:() =>({
        ms: 0,
        message: "",
        classes: "",
        isVisible: false
    }),
    actions: {
        showToast(ms: number, message: string, classes: string) {
            this.ms =  ms
            this.message = message
            this.classes = classes
            this.isVisible = true
            setTimeout(() => {
                this.classes = '-translate-y-28'
            }, 10);
            setTimeout(() => {
                this.classes = this.classes.replace('-translate-y-28', '')
            }, this.ms-500);
            setTimeout(() => {
                this.isVisible = false
            }, this.ms);
        }
    }
})
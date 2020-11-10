

function removeByIndex(array, index){
    return array.filter(function(elem, number){
        return index !== number;
    });
}
function insertion_Sort(nums) {
    for (let i = 1; i < nums.length; i++) {
        let j = i - 1
        let temp = nums[i]
        while (j >= 0 && nums[j] > temp) {
            nums[j + 1] = nums[j]
            j--
        }
        nums[j+1] = temp
    }
    return nums
}


function get1DArray(arr){

    var result = [];

    for (var x = 0; x < arr.length; x++){
        for (var y = 0; y < arr[x].length; y++){

            result.push(arr[x][y])

        }
    }

    return insertion_Sort(result)
}


function flaten(arr, result = []) {
    for (let i = 0, length = arr.length; i < length; i++) {
        const value = arr[i];
        if (Array.isArray(value)) {
            flaten(value, result);
        } else {
            result.push(value);
        }
    }
    return insertion_Sort(result);
}


function findByIndex(arr, x) {
    let start=0, end=arr.length-1;
    while (start<=end){
        let mid=Math.floor((start + end)/2);
        if (arr[mid]===x) return {"item":x,"index":mid};
        else if (arr[mid] < x)
            start = mid + 1;
        else
            end = mid - 1;
    }

    return false;
}



function replaceItem(arr,cuurent_item,new_item){
    for(let i=0 ; i<arr.length ; i++){
        if (arr[i]===cuurent_item){
            arr[i]=new_item
        }
    }
    return arr
}
function FindNumbers(text) {
    var numb = textt.match(/\d/g);
    return numb

}

//use set to remove dubliacte arrays
function removeDublicat(arr) {
    return Array.from(new Set(arr));


}
function remove_duplicates(arr) {
    var seen = {};
    var ret_arr = [];
    for (var i = 0; i < arr.length; i++) {
        if (!(arr[i] in seen)) {
            ret_arr.push(arr[i]);
            seen[arr[i]] = true;
        }
    }
    return insertion_Sort(ret_arr);

}



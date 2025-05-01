type Result = "pass" | "fail"

function isFailing(grade: number): Result {
    let result: Result;
    if (grade >= 70) {
        result = "pass"
    } else {
        result = "fail"
    }

    return result
}

console.log(isFailing(70))
console.log(isFailing(45))
console.log(isFailing(90))
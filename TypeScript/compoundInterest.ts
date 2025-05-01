// Formula: A = P(1 + r/n)^(nt)

function calculateCompoundInterest(principal: number, rate: number, time: number, compounded: number): number {
    return principal * (1 + rate/compounded) ** (compounded * time)
}

console.log(calculateCompoundInterest(520, 0.035, 2, 12))
export function cu(amount, is_fr) {
    if (is_fr) {
        return `${amount} ₮`;
    } else {
        return `₮ ${amount}`;
    }
}

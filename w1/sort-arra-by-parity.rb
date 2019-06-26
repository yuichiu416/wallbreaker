def sort_array_by_parity(a)
    return [] if a.length < 1
    left, right = 0, a.length - 1
    while left < right
        while left < a.length - 1 && a[left].even?
            left += 1
        end
        while right > 0 && a[right].odd?
            right -= 1
        end
        break if left >= right
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    end
    a
end

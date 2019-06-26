#Ruby one-liner

def flip_and_invert_image(a)
   a.map(&:reverse).map { |row| row.map { |ele| ele == 1? 0 : 1} }
end


#Normal approach
def flip_and_invert_image(a)
    a.each.with_index do |row, i|
        a[i] = row.reverse.map { |ele| ele == 1? 0:1}
    end
    a
end
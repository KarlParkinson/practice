require_relative 'stack'

def infix_postfix_convert(expr)
  prec = {"*" => 3, "/" => 3, "+" => 2, "-" => 2, "(" => 1}
  s = Stack.new
  operands = "+-/*()"
  str = ""
  expr.each_char do |c|
    if (operands.include?(c))
      if (c == '(')
        s.push(c)
      elsif (c == ')')
        op = s.pop
        while (op != '(')
          str += op
          op = s.pop
        end
      else
        while (!s.is_empty? and prec[c] < prec[s.peek])
          str += s.pop
        end
        s.push(c)
      end
    else
      str += c
    end
  end
  while (!s.is_empty?)
    str += s.pop
  end
  return str
end


begin
  inf = "2*3/4"
  puts infix_postfix_convert(inf)
end

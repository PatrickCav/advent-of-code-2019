use std::fs;

#[derive(Debug)]
struct Bounds {
    top: i32,
    right: i32,
    bottom: i32,
    left: i32
}

#[derive(Copy, Clone, Debug)]
struct Point {
    x: i32,
    y: i32
}

#[derive(Copy, Clone, Debug)]
struct Line {
    start: Point,
    end: Point
}

fn get_operations(input: String) -> Vec<String> {
    return input.split(",").map(|s| s.to_string()).collect();
}

fn apply_operation(input: String, start: &mut Point, current_bounds: &mut Bounds, cumulative_length: &mut Vec<i32>) {

    // println!("Input {}", input);

    let direction: String = input[..1].to_string();
    let length: i32 = input[1..].to_string().parse::<i32>().unwrap();

    cumulative_length.push(cumulative_length[cumulative_length.len() - 1] + length);

    // println!("Operation {}, length {}", direction, length);

    if direction == "R" {
        start.x = start.x + length;
        if current_bounds.right < start.x {
            current_bounds.right = start.x;
        }
    } else if direction == "L" {
        start.x = start.x - length;
        if current_bounds.left > start.x {
            current_bounds.left = start.x;
        }
    } else if direction == "U" {
        start.y = start.y + length;
        if current_bounds.top < start.y {
            current_bounds.top = start.y;
        }
    } else if direction == "D" {
        start.y = start.y - length;
        if current_bounds.bottom > start.y {
            current_bounds.bottom = start.y;
        }
    } else {
        println!("Other option {}", direction);
    }

    // println!("{:?}", &start);
}

fn intersection(first: Line, second: Line) -> Option<Point> {
    if first.start.x == first.end.x && second.start.y == second.end.y {
        // first vertical, second horizontal
        let x = first.start.x;
        let y = second.start.y;
        if ((second.start.x < x && x < second.end.x) || (second.end.x < x && x < second.start.x)) && ((first.end.y < y && y < first.start.y) || (first.start.y < y && y < first.end.y)) {
            println!("Intersection found in lines {:?} {:?}", first, second);
            return Some(Point {x: x, y: y});
        } else {
            return None;
        }
    } else if first.start.y == first.end.y && second.start.x == second.end.x {
        // first horizontal, second vertical
        let x = second.start.x;
        let y = first.start.y;
        if ((first.start.x < x && x < first.end.x) || (first.end.x < x && x < first.start.x)) && ((second.end.y < y && y < second.start.y) || (second.start.y < y && y < second.end.y)) {
            println!("Intersection found in lines {:?} {:?}", first, second);
            return Some(Point {x: x, y: y});
        } else {
            return None;
        }
    } else {
        // lines parallel
        return None;
    }
}

fn manhattanOriginDistance(point: &Point) -> i32 {
    return point.x.abs() + point.y.abs();
}

fn manhattanDistance(point_a: &Point, point_b: &Point) -> i32 {
    return (point_a.x - point_b.x).abs() + (point_a.y - point_b.y).abs();
}

fn main() {
    // let first: Vec<String> = get_operations("R8,U5,L5,D3".to_string());
    // let second: Vec<String> = get_operations("U7,R6,D4,L4".to_string());
    
    // let first: Vec<String> = get_operations("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".to_string());
    // let second: Vec<String> = get_operations("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".to_string());
    
    // println!("{:?}", test_first);
    // println!("{:?}", test_second);

    let data = fs::read_to_string("day3_input.txt").expect("Unable to read file");
    println!("{}", data);

    let instruction_set: Vec<String> = data.split("\n").map(|s| s.to_string()).collect();

    println!("Lines {}", instruction_set.len());

    let first: Vec<String> = get_operations(instruction_set[0].to_string());
    let second: Vec<String> = get_operations(instruction_set[1].to_string());

    let mut first_points: Vec<Point> = Vec::new();
    let mut first_cumulative_length: Vec<i32> = Vec::new();
    let mut first_bounds = Bounds{top: 0, right: 0, bottom: 0, left: 0 };
    let mut first_start = Point{x: 0, y: 0};
    first_points.push(first_start);
    first_cumulative_length.push(0);

    for i in 0..first.len() {
        let input = &first[i];
        apply_operation(input.to_string(), &mut first_start, &mut first_bounds, &mut first_cumulative_length);
        first_points.push(first_start);
    }

    let mut second_points: Vec<Point> = Vec::new();
    let mut second_cumulative_length: Vec<i32> = Vec::new();
    let mut second_bounds = Bounds{top: 0, right: 0, bottom: 0, left: 0 };
    let mut second_start = Point{x: 0, y: 0};
    second_points.push(second_start);
    second_cumulative_length.push(0);

    let mut intersections: Vec<Point> = Vec::new();

    let mut smallest_total: i32 = std::i32::MAX;

    for i in 0..second.len() {
        let input = &second[i];
        apply_operation(input.to_string(), &mut second_start, &mut second_bounds, &mut second_cumulative_length);
        second_points.push(second_start);

        // if second_start.x < first_bounds.right && second_start.x > first_bounds.left && 
            // second_start.y < first_bounds.top && second_start.y > first_bounds.bottom {
            for j in 1..first_points.len() {
                let first = Line{start: first_points[j - 1], end: first_points[j]};
                let second = Line{start: second_points[i], end: second_points[i + 1]};
                if let Some(intersection) = intersection(first, second) {
                    println!("Intersection found: {:?}", intersection);
                    intersections.push(intersection);
                    let first_length = first_cumulative_length[j - 1] + manhattanDistance(&first.start, &intersection);
                    let second_length = second_cumulative_length[i] + manhattanDistance(&second.start, &intersection);
                    println!("First length {}", first_length);
                    println!("Second length {}", second_length);
                    let total = first_length + second_length;
                    if total < smallest_total {
                        smallest_total = total;
                    }
                }
            }
        // }
    }

    println!("Shortest Distance {}", smallest_total);

    // println!("{:?}", first_bounds);
    // println!("{:?}", first_points);
    // println!("{:?}", second_points);
    // println!("{:?}", intersections);
}
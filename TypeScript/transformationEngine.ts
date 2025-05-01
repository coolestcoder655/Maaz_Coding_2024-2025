// @ts-check

class Shape {
    points: any[]; // Define the points property

    /** @param {any[]} Coordinents Of The Shape */

    constructor(...args: any[]) {
        this.points = args;
    }

    translate(xAxis: number, yAxis: number): any[] {
        for (let i = 0; i < this.points.length; i++) {
            // [[4, 5], [8, 1]]
            let point = this.points[i];
            point[0] += xAxis;
            point[1] += yAxis;
        }

        return this.points;
    }

    reflect(axis: string): any[] {
        if (axis === "x") {
            for (let i = 0; i < this.points.length; i++) {
                let point = this.points[i];

                point[1] = -(point[1]);
            }
        } else if (axis === "y") {
            for (let i = 0; i< this.points.length; i++) {
                let point = this.points[i];

                point[0] = -(point[0]);
            }
        }

        return this.points;
    }


    rotation(degrees: number): any[] {
        if (degrees === 90) {
            for (let i = 0; i < this.points.length; i++) {
                // (-y, x)
                let point: any[] = this.points[i];

                point = [-(point[1]), point[0]];
            }

        } else if (degrees === 180) {
            for (let i = 0; i < this.points.length; i++) {
                //  (-x, -y)
                let point: any[] = this.points[i];

                point = [-(point[0]), -(point[1])];
            }

        } else if (degrees === 270) {
            for (let i = 0; i < this.points.length; i++) {
                // (y, -x)
                let point: any[] = this.points[i];

                point = [point[1], -(point[0])];
            }

        } else if (degrees === 360) {
            for (let i = 0; i < this.points.length; i++) {
                // (x, y)
                let point: any[] = this.points[i];

                point = [point[0], point[1]];
            }
        }

        return this.points;
    }


    dilate(dilatonFactor: number): any[] {
        for (let i = 0; i < this.points.length; i++) {
            let point: any[] = this.points[i];

            point = [(point[0] * dilatonFactor), (point[1] * dilatonFactor)];
        }

        return this.points;
    } 
};

const newPoints = [
    [4, 5],
    [8, 1],
    [2, 3],
    [6, 7]
];

let triangle1 = new Shape(newPoints);

console.log(`Translation by 2 on x-axis and 3 on y-axis: ${triangle1.translate(2, 3)}`); // [[6, 8], [10, 4], [4, 6], [8, 10]]

console.log(`Reflection on x-axis: ${triangle1.reflect("x")}`); // [[6, -8], [10, -4], [4, -6], [8, -10]]

console.log(`Reflection on y-axis: ${triangle1.reflect("y")}`); // [[-6, -8], [-10, -4], [-4, -6], [-8, -10]]

console.log(`Rotation by 90 degrees: ${triangle1.rotation(90)}`); // [[-8, 6], [-4, 10], [-6, 4], [-10, 8]]

console.log(`Rotation by 180 degrees: ${triangle1.rotation(180)}`); // [[8, 6], [4, 10], [6, 4], [10, 8]]

console.log(`Rotation by 270 degrees: ${triangle1.rotation(270)}`); // [[6, -8], [10, -4], [4, -6], [8, -10]]

console.log(`Rotation by 360 degrees: ${triangle1.rotation(360)}`); // [[6, 8], [10, 4], [4, 6], [8, 10]]

console.log(`Dilation by 2: ${triangle1.dilate(2)}`); // [[12, 16], [20, 8], [8, 12], [16, 20]]

console.log(`Dilation by 3: ${triangle1.dilate(3)}`); // [[18, 24], [30, 12], [12, 18], [24, 30]]
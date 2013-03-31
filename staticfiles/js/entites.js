function Coordinate (latitude, longtitude) {
    this.latitude = latitude;
    this.longtitude = longtitude;
    return this;
}


function Route (coordinate_start, coordinate_finish) {
    this.coordinate_start = coordinate_start;
    this.coordinate_finish = coordinate_finish;
    return this;
}
 
export class Product {
  constructor(
    public name: string,
    public description: string,
    public imageUrl: string,
    public _id?: number,
    public updatedAt?: Date,
    public createdAt?: Date,
    public lastUpdatedBy?: number,
    public createdBy?: number
  ) { }
}

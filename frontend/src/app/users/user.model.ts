export class User {
  constructor(
    public firstName: string,
    public lastName: string,
    public username: string,
    public _id?: number,
    public updatedAt?: Date,
    public createdAt?: Date,
    public lastUpdatedBy?: number,
    public createdBy?: number
  ) { }
}

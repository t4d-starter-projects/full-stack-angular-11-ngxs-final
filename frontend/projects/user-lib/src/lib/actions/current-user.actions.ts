import { ICurrentUser } from '../models/CurrentUser';

export class SetCurrentUser {
  static readonly type = '[User] Set Current User';
  constructor(public currentUser: ICurrentUser) { }
}

export class ClearCurrentUser {
  static readonly type = '[User] Clear Current User';
}

export class LoginUser {
  static readonly type = '[User] Login User';
  constructor(public username: string, public password: string) { }
}

export class LogoutUser {
  static readonly type = '[User] Logout User';
}
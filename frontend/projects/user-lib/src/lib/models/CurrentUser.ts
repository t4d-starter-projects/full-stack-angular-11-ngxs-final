import { intersection } from 'lodash-es';

export interface ICurrentUser {
  username: string;
  userKind: string;
  displayName: string;
  roles: string[];
}

export class CurrentUser implements ICurrentUser {

  public username: string;
  public userKind: string;
  public displayName: string;
  public roles: string[];

  constructor(username: string, userKind: string, displayName: string) {
    this.username = username;
    this.userKind = userKind;
    this.displayName = displayName;
    this.roles = [];
  }

  public addRole(roleName: string): CurrentUser {
    if (!roleName) throw new Error('role name cannot be empty');
    this.roles.push(roleName);
    return this;
  }

  public hasRole(roleNames: string[]): boolean {
    return intersection(this.roles, roleNames).length > 0;
  }

}
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { Employee } from '../models/Employee';

@Injectable({
  providedIn: 'root'
})
export class EmployeesService {

  constructor(private httpClient: HttpClient) { }

  all(): Observable<Employee[]> {
    return this.httpClient.get<Employee[]>('/api/employees').pipe(
      catchError(() => {
        throw Error('Unable to download employees');
      })
    );
  }
}

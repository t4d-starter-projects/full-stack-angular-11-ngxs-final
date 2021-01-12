import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { Category } from '../models/Category';

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {

  constructor(private httpClient: HttpClient) { }

  all(): Observable<Category[]> {
    return this.httpClient.get<Category[]>('/api/categories').pipe(
      catchError(() => {
        throw Error('Unable to download categories');
      })
    );
  }
}
